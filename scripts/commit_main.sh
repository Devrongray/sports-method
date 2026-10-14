#!/usr/bin/env bash
# Commit a results directory to main from inside GitHub Actions, retrying if
# another workflow pushed first. Pushes made with GITHUB_TOKEN do not trigger
# further workflow runs, so this cannot loop.
set -euo pipefail
DIR="$1"
MSG="$2"
git config user.name "method-bot"
git config user.email "method-bot@users.noreply.github.com"
git add "$DIR"
if git diff --cached --quiet; then
  echo "nothing to commit"; exit 0
fi
git commit -qm "$MSG"
for i in 1 2 3 4 5; do
  if git push origin HEAD:main; then exit 0; fi
  echo "push rejected, rebasing (attempt $i)"
  git pull --rebase -q origin main
done
echo "could not push after 5 attempts" >&2
exit 1
