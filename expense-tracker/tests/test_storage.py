import json
from datetime import date
from decimal import Decimal

import pytest

from expense_tracker.exceptions import StorageError
from expense_tracker.models import Expense
from expense_tracker.storage import load_expenses, save_expenses


def test_save_and_load_expenses(tmp_path):
    file_path = tmp_path / "expenses.json"

    expenses = [
        Expense(
            id=1,
            description="Lunch",
            category="Food",
            amount=Decimal("120.50"),
            date=date(2026, 10, 28),
        )
    ]

    save_expenses(expenses, file_path)
    loaded = load_expenses(file_path)

    assert loaded == expenses


def test_load_expenses_returns_empty_list_when_file_missing(tmp_path):
    file_path = tmp_path / "missing.json"

    assert load_expenses(file_path) == []


def test_load_expenses_rejects_malformed_json(tmp_path):
    file_path = tmp_path / "expenses.json"
    file_path.write_text("{invalid json", encoding="utf-8")

    with pytest.raises(StorageError):
        load_expenses(file_path)


def test_load_expenses_rejects_non_list_json(tmp_path):
    file_path = tmp_path / "expenses.json"
    file_path.write_text(json.dumps({"id": 1}), encoding="utf-8")

    with pytest.raises(StorageError):
        load_expenses(file_path)


def test_load_expenses_rejects_invalid_amount(tmp_path):
    file_path = tmp_path / "expenses.json"
    file_path.write_text(
        json.dumps(
            [
                {
                    "id": 1,
                    "description": "Lunch",
                    "category": "Food",
                    "amount": "-10",
                    "date": "2026-10-28",
                }
            ]
        ),
        encoding="utf-8",
    )

    with pytest.raises(StorageError):
        load_expenses(file_path)
