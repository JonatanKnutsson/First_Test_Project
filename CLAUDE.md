# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Python 3.13 project (Anaconda environment on Windows). The repo is new — ask before introducing a package layout, dependency manager, or framework.

## Tooling

- Lint/format: `ruff check --fix` and `ruff format` (runs automatically on edited `.py` files via a hook)
- Tests: `pytest`; single test with `pytest path/to/test_file.py -k test_name`

## Git

- Never commit to `main` directly. Branch off `main` (e.g. `feature/<short-name>`, `fix/<short-name>`) and open a pull request on GitHub (`origin` = JonatanKnutsson/First_Test_Project).
