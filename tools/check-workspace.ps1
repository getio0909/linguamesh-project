[CmdletBinding()]
param(
    [switch]$RequireRepositories
)

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $PSScriptRoot
$ValidatorArguments = @(
    (Join-Path $PSScriptRoot "check_workspace.py"),
    "--project-root",
    $ProjectRoot
)
if ($RequireRepositories) {
    $ValidatorArguments += "--require-repositories"
}

$PythonCommand = Get-Command python -ErrorAction SilentlyContinue
if ($PythonCommand) {
    & $PythonCommand.Source @ValidatorArguments
}
else {
    $PythonLauncher = Get-Command py -ErrorAction SilentlyContinue
    if (-not $PythonLauncher) {
        throw "Validation failed: Python 3.11 or newer is required."
    }
    & $PythonLauncher.Source -3 @ValidatorArguments
}
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

if (Get-Command git -ErrorAction SilentlyContinue) {
    git -C $ProjectRoot rev-parse --is-inside-work-tree 2>$null | Out-Null
    if ($LASTEXITCODE -eq 0) {
        git -C $ProjectRoot diff --check
        if ($LASTEXITCODE -ne 0) {
            exit $LASTEXITCODE
        }
    }
}

