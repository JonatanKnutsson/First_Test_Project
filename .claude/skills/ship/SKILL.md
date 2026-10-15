---
name: ship
description: Commit the current changes on a feature branch, push it, and open a GitHub pull request against main.
disable-model-invocation: true
---

Ship the current working-tree changes as a pull request. Optional argument: $ARGUMENTS (branch name or short description).

1. Run `git status` and `git diff` to understand the changes. If there are none, stop and say so.
2. If on `main`, create a branch: `feature/<short-name>` (or `fix/<short-name>` for bug fixes), derived from $ARGUMENTS or the diff.
3. Run `ruff check .` and `pytest` (if tests exist). If either fails, report it and stop.
4. Stage the relevant files (not unrelated or secret files) and commit with a concise message describing why.
5. Push with `git push -u origin <branch>`.
6. Open the PR with `gh pr create --base main` with a short title and a body summarizing the change and how it was tested. If `gh` is not installed, give the user the compare URL instead: `https://github.com/JonatanKnutsson/First_Test_Project/compare/<branch>?expand=1`.
7. Report the PR URL.
