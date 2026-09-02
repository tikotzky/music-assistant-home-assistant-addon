#!/usr/bin/env bash
# Merge the upstream add-on repository into this branch and re-apply the 24six overlay.
#
# The merge takes upstream's tree wholesale, restores the files that belong to this fork
# (the 24six tooling and the add-on changelog) and then runs 24six/apply_overlay.py, which
# writes the 24six identity back over upstream's files and drops the add-ons this fork does
# not ship. The result is committed as a merge of upstream so history records what was
# synced. Nothing is committed when the tree would not change. Nothing is pushed.
#
# Usage: 24six/sync_upstream.sh [<upstream ref>]   (default: upstream/main)

set -euo pipefail

upstream_ref="${1:-upstream/main}"
addon_folder=music_assistant
fork_paths=(24six .github/workflows/sync-upstream.yml "$addon_folder/CHANGELOG.md")

cd "$(git rev-parse --show-toplevel)"

if [ -n "$(git status --porcelain)" ]; then
  echo "The working tree must be clean before syncing" >&2
  exit 1
fi

# The version names this fork's container image, so it must survive the upstream tree.
version="$(git show "HEAD:$addon_folder/config.yaml" | sed -n 's/^version: //p')"
if [ -z "$version" ]; then
  echo "No version found in $addon_folder/config.yaml" >&2
  exit 1
fi

# `-s ours` only records the merge parent; the tree is rebuilt from upstream below.
if ! git merge-base --is-ancestor "$upstream_ref" HEAD; then
  git merge --no-ff --no-commit -s ours "$upstream_ref" > /dev/null
fi
git restore --source="$upstream_ref" --staged --worktree -- .
git restore --source=HEAD --staged --worktree -- "${fork_paths[@]}"
python3 24six/apply_overlay.py --version "$version"
git add --all

if git diff --cached --quiet HEAD; then
  git merge --abort 2> /dev/null || true
  echo "Already in sync with $upstream_ref"
  exit 0
fi

git commit --quiet --message "Sync with upstream $(git rev-parse --short "$upstream_ref")"
echo "Synced with $upstream_ref:"
git show --stat --oneline HEAD | tail -n +2
