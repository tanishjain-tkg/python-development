from datetime import date
from decimal import Decimal

import pytest

from expense_tracker.exceptions import ExpenseNotFoundError, InvalidExpenseError
from expense_tracker.models import Expense
from expense_tracker.services import (
    add_expense,
    calculate_total,
    delete_expense,
    list_expenses,
)


def test_add_expense_creates_expense():
    expenses = []

    expense = add_expense(
        expenses=expenses,
        description="Lunch",
        category="Food",
        amount="120.50",
        expense_date=date(2026, 10, 28),
    )

    assert expense.id == 1
    assert expense.description == "Lunch"
    assert expense.category == "Food"
    assert expense.amount == Decimal("120.50")
    assert expense.date == date(2026, 10, 28)
    assert expenses == [expense]


def test_add_expense_strips_whitespace():
    expenses = []

    expense = add_expense(
        expenses=expenses,
        description="  Lunch  ",
        category="  Food  ",
        amount="50",
    )

    assert expense.description == "Lunch"
    assert expense.category == "Food"


def test_add_expense_rejects_empty_description():
    expenses = []

    with pytest.raises(InvalidExpenseError):
        add_expense(expenses, "", "Food", "50")


def test_add_expense_rejects_empty_category():
    with pytest.raises(InvalidExpenseError):
        add_expense([], "Lunch", "   ", "50")


@pytest.mark.parametrize(
    "amount",
    ["0", "-10", "abc", "NaN", "Infinity"],
)
def test_add_expense_rejects_invalid_amount(amount):
    with pytest.raises(InvalidExpenseError):
        add_expense([], "Lunch", "Food", amount)


def test_add_expense_generates_next_id():
    expenses = [
        Expense(
            id=1,
            description="Lunch",
            category="Food",
            amount=Decimal(100),
            date=date(2026, 10, 28),
        ),
        Expense(
            id=3,
            description="Bus",
            category="Travel",
            amount=Decimal(30),
            date=date(2026, 10, 28),
        ),
    ]

    expense = add_expense(expenses, "Coffee", "Food", "40")

    assert expense.id == 4


def test_list_expenses_returns_copy():
    expenses = [
        Expense(
            id=1,
            description="Lunch",
            category="Food",
            amount=Decimal(100),
            date=date(2026, 10, 28),
        )
    ]

    result = list_expenses(expenses)

    assert result == expenses
    assert result is not expenses


def test_calculate_total():
    expenses = [
        Expense(1, "Lunch", "Food", Decimal("100.50"), date(2026, 10, 28)),
        Expense(2, "Bus", "Travel", Decimal("30.00"), date(2026, 10, 28)),
    ]

    assert calculate_total(expenses) == Decimal("130.50")


def test_calculate_total_with_no_expenses():
    assert calculate_total([]) == Decimal("0.00")


def test_delete_expense_removes_and_returns_expense():
    expenses = [
        Expense(1, "Lunch", "Food", Decimal(100), date(2026, 10, 28)),
        Expense(2, "Bus", "Travel", Decimal(30), date(2026, 10, 28)),
    ]

    deleted = delete_expense(expenses, 1)

    assert deleted.id == 1
    assert len(expenses) == 1
    assert expenses[0].id == 2


def test_delete_expense_raises_when_not_found():
    with pytest.raises(ExpenseNotFoundError):
        delete_expense([], 99)
