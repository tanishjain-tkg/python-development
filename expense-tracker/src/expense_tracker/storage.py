import json
import logging
from datetime import date
from decimal import Decimal
from pathlib import Path

from .exceptions import StorageError
from .models import Expense

logger = logging.getLogger(__name__)

DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "expenses.json"


def load_expenses(
    file_path: Path = DATA_FILE,
) -> list[Expense]:
    if not file_path.exists():
        logger.info("Expense file does not exist; starting empty.")
        return []

    try:
        with file_path.open("r", encoding="utf-8") as file:
            records = json.load(file)

        if not isinstance(records, list):
            raise TypeError("Expense data must be a JSON list.")

        expenses = []

        for record in records:
            if not isinstance(record, dict):
                raise TypeError("Each expense must be a JSON object.")

            expense = Expense(
                id=int(record["id"]),
                description=record["description"],
                category=record["category"],
                amount=Decimal(record["amount"]),
                date=date.fromisoformat(record["date"]),
            )

            if (
                not isinstance(expense.description, str)
                or not isinstance(expense.category, str)
                or not expense.description.strip()
                or not expense.category.strip()
                or not expense.amount.is_finite()
                or expense.amount <= 0
                or expense.id <= 0
            ):
                raise ValueError("Invalid expense record.")

            expenses.append(expense)

        logger.info("Loaded %s expense(s).", len(expenses))
        return expenses

    except (
        OSError,
        json.JSONDecodeError,
        KeyError,
        TypeError,
        ValueError,
        ArithmeticError,
    ) as exc:
        logger.exception("Failed to load expenses from %s", file_path)
        raise StorageError(f"Could not read expense data from {file_path}.") from exc


def save_expenses(
    expenses: list[Expense],
    file_path: Path = DATA_FILE,
) -> None:
    records = [
        {
            "id": expense.id,
            "description": expense.description,
            "category": expense.category,
            "amount": str(expense.amount),
            "date": expense.date.isoformat(),
        }
        for expense in expenses
    ]

    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)

        with file_path.open("w", encoding="utf-8") as file:
            json.dump(records, file, indent=4)

        logger.info("Saved %s expense(s).", len(expenses))

    except OSError as exc:
        logger.exception("Failed to save expenses to %s", file_path)
        raise StorageError(f"Could not save expense data to {file_path}.") from exc
