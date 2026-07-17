# GitHub Bootstrap

These commands are the reviewed bootstrap procedure. Repository existence and publication evidence belongs in `IMPLEMENTATION_STATUS.md`; do not infer current remote state from this procedure alone. Run writes only with an authenticated GitHub CLI session and explicit authorization. The commands resolve the owner at runtime and never embed a credential.

```sh
gh auth status
GITHUB_OWNER="$(gh api user --jq '.login')"
test -n "$GITHUB_OWNER"

gh repo view "$GITHUB_OWNER/linguamesh-project"
gh repo view "$GITHUB_OWNER/linguamesh-core"
gh repo view "$GITHUB_OWNER/linguamesh-l10n"
gh repo view "$GITHUB_OWNER/linguamesh-android"
gh repo view "$GITHUB_OWNER/linguamesh-windows"
gh repo view "$GITHUB_OWNER/linguamesh-macos"
gh repo view "$GITHUB_OWNER/linguamesh-linux"
```

For each repository that is confirmed missing, prepare and verify the local `main` branch before creating the public remote. Substitute one canonical name at a time:

```sh
REPOSITORY_NAME="linguamesh-core"
REPOSITORY_DESCRIPTION="LinguaMesh provider-neutral Rust translation core"
git -C "../$REPOSITORY_NAME" status --short
git -C "../$REPOSITORY_NAME" branch --show-current
git -C "../$REPOSITORY_NAME" log -1 --oneline
gh repo create "$GITHUB_OWNER/$REPOSITORY_NAME" --public --description "$REPOSITORY_DESCRIPTION" --source "../$REPOSITORY_NAME" --remote origin --push
gh repo edit "$GITHUB_OWNER/$REPOSITORY_NAME" --enable-issues --add-topic linguamesh --add-topic translation
gh repo view "$GITHUB_OWNER/$REPOSITORY_NAME" --json nameWithOwner,visibility,defaultBranchRef,url
```

Recommended descriptions:

| Repository | Description |
| --- | --- |
| `linguamesh-project` | LinguaMesh architecture, policy, roadmap, and release coordination |
| `linguamesh-core` | LinguaMesh provider-neutral Rust translation core |
| `linguamesh-l10n` | LinguaMesh canonical localization data and generators |
| `linguamesh-android` | LinguaMesh native Android client |
| `linguamesh-windows` | LinguaMesh native Windows client |
| `linguamesh-macos` | LinguaMesh native macOS client |
| `linguamesh-linux` | LinguaMesh native Linux client |

Before every creation, repeat the remote lookup and local status checks. Never create an empty remote when a prepared local repository can be pushed. Do not force-push, rewrite history, delete a repository, or publish releases from this procedure.
