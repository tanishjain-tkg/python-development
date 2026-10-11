# Python Expense Tracker

A command-line expense tracking application built with Python.

## Features

- Add expenses with a description, category, and amount.
- View all recorded expenses.
- Calculate total spending.
- Validate user input and reject invalid amounts.
- Use Python's `Decimal` for monetary calculations.

## Tech Stack

- Python 3.14
- Standard Python library
- Git and GitHub

## Project Structure

```text
expense-tracker/
├── src/
│   └── expense_tracker/
│       ├── __init__.py
│       └── main.py
├── tests/
├── data/
├── .gitignore
├── pyproject.toml
└── README.md
```

## Setup

Clone the repository and navigate to the project directory.

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project in editable mode:

```bash
python -m pip install -e .
```

## Run the Application

```bash
expense-tracker
```

Alternatively:

```bash
python -m expense_tracker.main
```

## Current Limitations

- Expenses are stored in memory and are lost when the application exits.
- JSON persistence, automated tests, and expense editing are planned for future iterations.

## Learning Goals

Practice Python fundamentals, CLI development, package structure, input validation, Git workflows, and software testing.