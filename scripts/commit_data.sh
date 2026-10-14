#!/usr/bin/env bash
# Commit a directory of recorded data to the `data` branch of this repo.
# Creates the branch on first use. Run from the repo root inside GitHub Actions.
#
# actions/checkout fetches only the triggering branch, so the data branch is
# fetched explicitly here before a worktree is made from it.
set -euo pipefail
SRC="${1:-data}"
BRANCH="${DATA_BRANCH:-data}"
REMOTE="${REMOTE:-origin}"

if [ ! -d "$SRC" ] || [ -z "$(find "$SRC" -type f | head -n 1)" ]; then
  echo "nothing recorded under $SRC"; exit 0
fi

git config user.name "method-bot"
git config user.email "method-bot@users.noreply.github.com"

STORE="$(mktemp -d)"
if git ls-remote --exit-code --heads "$REMOTE" "$BRANCH" >/dev/null 2>&1; then
  git fetch --depth 1 "$REMOTE" "+refs/heads/$BRANCH:refs/remotes/$REMOTE/$BRANCH"
  git worktree add --detach "$STORE" "refs/remotes/$REMOTE/$BRANCH"
  (cd "$STORE" && git checkout -B "$BRANCH")
else
  git worktree add --detach "$STORE"
  (cd "$STORE" && git checkout --orphan "$BRANCH" && git rm -rfq . || true)
fi

mkdir -p "$STORE/$SRC"
cp -R "$SRC"/. "$STORE/$SRC"/
(
  cd "$STORE"
  git add -A "$SRC"
  if git diff --cached --quiet; then
    echo "no new data"
  else
    git commit -qm "data: $(date -u +%FT%TZ) $(find "$SRC" -type f | wc -l) files"
    for i in 1 2 3 4 5; do
      if git push "$REMOTE" "HEAD:$BRANCH"; then exit 0; fi
      echo "push rejected, rebasing (attempt $i)"
      git fetch --depth 1 "$REMOTE" "$BRANCH"
      git rebase -q FETCH_HEAD
    done
    echo "could not push after 5 attempts" >&2
    exit 1
  fi
)
git worktree remove --force "$STORE"
