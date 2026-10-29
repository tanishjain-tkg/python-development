# Python Expense Tracker

A command-line expense tracking application built with Python. The project demonstrates Python packaging, input validation, JSON persistence, custom exceptions, logging, and automated testing.

## Features

- Add expenses with a description, category, amount, and date.
- View recorded expenses.
- Calculate total spending.
- Delete expenses by ID.
- Validate descriptions, categories, and monetary amounts.
- Use `Decimal` for precise monetary calculations.
- Persist expenses in a JSON file.
- Handle invalid input and storage errors with custom exceptions.
- Run automated tests with pytest.

## Tech Stack

- Python 3.10+
- pytest for automated testing
- Ruff for linting and formatting
- JSON for local data persistence
- Git and GitHub for version control

## Project Structure

```text
expense-tracker/
├── src/
│   └── expense_tracker/
│       ├── __init__.py
│       ├── main.py
│       ├── models.py
│       ├── services.py
│       ├── storage.py
│       └── exceptions.py
├── tests/
│   ├── __init__.py
│   ├── test_services.py
│   └── test_storage.py
├── data/
├── .gitignore
├── pyproject.toml
└── README.md
```

## Prerequisites

- Python 3.10 or newer
- Git

## Setup on Windows with Git Bash

Clone the repository and navigate to the project directory.

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it in Git Bash:

```bash
source .venv/Scripts/activate
```

Install the project and development dependencies:

```bash
python -m pip install -e ".[dev]"
```

## Run the Application

```bash
expense-tracker
```

Alternatively, run the module:

```bash
python -m expense_tracker.main
```

## Run Tests

Run the complete test suite:

```bash
python -m pytest -v
```

## Check Code Quality

Run Ruff's linter:

```bash
python -m ruff check .
```

Check formatting:

```bash
python -m ruff format --check .
```

To apply automatic lint fixes and formatting:

```bash
python -m ruff check . --fix
python -m ruff format .
```

## Data Storage

Expenses are stored locally in `data/expenses.json`. The application loads saved expenses when it starts and writes updates when expenses are added or deleted.

The data file is generated at runtime and should not be committed to version control.

## Learning Outcomes

This project provides practical experience with:

- Python modules, packages, and virtual environments.
- Dataclasses, type hints, and `Decimal`.
- Separation of business logic from CLI and storage code.
- JSON serialization and filesystem operations.
- Custom exceptions and logging.
- Unit testing with pytest and temporary files.
- Linting, formatting, and GitHub pull request workflows.
