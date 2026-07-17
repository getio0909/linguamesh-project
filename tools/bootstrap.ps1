[CmdletBinding()]
param(
    [string]$Owner = $env:GITHUB_OWNER,
    [switch]$CheckOnly,
    [switch]$FetchExisting
)

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $PSScriptRoot
$Workspace = Split-Path -Parent $ProjectRoot
$Repositories = @(
    "linguamesh-project",
    "linguamesh-core",
    "linguamesh-l10n",
    "linguamesh-android",
    "linguamesh-windows",
    "linguamesh-macos",
    "linguamesh-linux"
)
$Missing = 0

foreach ($Repository in $Repositories) {
    $Target = Join-Path $Workspace $Repository
    if (Test-Path -LiteralPath $Target -PathType Container) {
        Write-Output "Existing repository preserved: $Target"
        if ($FetchExisting -and (Test-Path -LiteralPath (Join-Path $Target ".git") -PathType Container)) {
            git -C $Target fetch --prune
            if ($LASTEXITCODE -ne 0) {
                throw "Bootstrap failed: Git fetch failed for $Repository."
            }
            Write-Output "Fetched remote references: $Repository"
        }
        continue
    }

    $Missing += 1
    if ($CheckOnly) {
        Write-Output "Missing repository: $Target"
        continue
    }
    if ([string]::IsNullOrWhiteSpace($Owner)) {
        throw "Bootstrap failed: -Owner or GITHUB_OWNER is required to clone $Repository."
    }
    if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
        throw "Bootstrap failed: GitHub CLI is required to clone missing repositories."
    }
    gh repo view "$Owner/$Repository" | Out-Null
    if ($LASTEXITCODE -ne 0) {
        throw "Bootstrap failed: remote repository is unavailable: $Owner/$Repository"
    }
    gh repo clone "$Owner/$Repository" $Target
    if ($LASTEXITCODE -ne 0) {
        throw "Bootstrap failed: clone failed for $Repository."
    }
    Write-Output "Cloned repository: $Repository"
}

if ($CheckOnly -and $Missing -gt 0) {
    throw "Bootstrap check failed: $Missing canonical repositories are missing."
}

& (Join-Path $ProjectRoot "tools/check-workspace.ps1") -RequireRepositories
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}
Write-Output "Workspace bootstrap completed."
