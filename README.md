# System Monitor

A desktop application that monitors CPU, RAM, and disk usage in real time, built with Python, ttkbootstrap, and psutil.

---

## Requirements

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) (package manager)

---

## Setup

```bash
git clone https://github.com/r4muba/SysWatch
cd SysWatch
uv sync
```

> `uv sync` reads the lockfile and installs the exact same dependencies for everyone — no version mismatches.

## Run

```bash
uv run python main.py
```

---

## Project Structure

```
project/
├── main.py            
├── gui.py             ttkbootstrap interface
    |──── GeneralDashboard      General dashboard
    |──── Active Process        Information of processs (PID, status, etc) + dynamic
    |──── Memory RAM            Overall Information + pages faults
├── controller.py      Bridges GUI, lets try to implement this way


├── pyproject.toml     project dependencies (commit this)
├── uv.lock            pinned versions for everyone (commit this)
├── .gitignore         excludes .venv and other local files
└── README.md          
```

Overall, all the gui classes should not have any logical and operational statements they should try to call a function in controller that would return some valueable information that allows to perform the expected changes in the visualization. This is hard to accomplish but lets try team
---

## Architecture

This project uses a **one class per file** rule to minimize merge conflicts — each team member owns one file.


## Team Rules

| Rule | Why |
|---|---|
| One class per file | Changes stay isolated, fewer merge conflicts |
| Always `uv add <package>` | Keeps `pyproject.toml` and `uv.lock` in sync |
| Never `pip install` directly | pip bypasses the lockfile — teammates won't get the package |
| Commit `pyproject.toml` and `uv.lock` | This is how everyone gets the same environment |
| Never commit `.venv/` | Generated locally by `uv sync`, platform-specific |
| Never touch the GUI from a background thread | Will cause random crashes |
| No Vibecoding | Dont push --force git
| In Logan we trust | We need to improve this desing to allow threading
---

## Adding a New Dependency

```bash
uv add <package-name>
git add pyproject.toml uv.lock
git commit -m "add <package-name>"
```

## Pulling Changes from Teammates

```bash
git pull
uv sync   # always run this after pulling — someone may have added a package
```
