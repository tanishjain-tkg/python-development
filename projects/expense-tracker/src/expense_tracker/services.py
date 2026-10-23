import logging
from datetime import date
from decimal import Decimal, InvalidOperation

from .exceptions import ExpenseNotFoundError, InvalidExpenseError
from .models import Expense

logger = logging.getLogger(__name__)


def add_expense(
    expenses: list[Expense],
    description: str,
    category: str,
    amount: Decimal | str,
    expense_date: date | None = None,
) -> Expense:
    description = description.strip()
    category = category.strip()

    if not description:
        raise InvalidExpenseError("Description cannot be empty.")

    if not category:
        raise InvalidExpenseError("Category cannot be empty.")

    try:
        amount = Decimal(str(amount))
    except (InvalidOperation, ValueError):
        raise InvalidExpenseError("Amount must be a valid number.") from None

    if not amount.is_finite() or amount <= 0:
        raise InvalidExpenseError("Amount must be positive and finite.")

    next_id = max((expense.id for expense in expenses), default=0) + 1

    expense = Expense(
        id=next_id,
        description=description,
        category=category,
        amount=amount,
        date=expense_date or date.today(),
    )

    expenses.append(expense)
    logger.info("Added expense with ID %s", expense.id)
    return expense


def list_expenses(expenses: list[Expense]) -> list[Expense]:
    return list(expenses)


def calculate_total(expenses: list[Expense]) -> Decimal:
    return sum(
        (expense.amount for expense in expenses),
        start=Decimal("0.00"),
    )


def delete_expense(
    expenses: list[Expense],
    expense_id: int,
) -> Expense:
    for index, expense in enumerate(expenses):
        if expense.id == expense_id:
            deleted = expenses.pop(index)
            logger.info("Deleted expense with ID %s", expense_id)
            return deleted

    raise ExpenseNotFoundError(
        f"Expense with ID {expense_id} not found."
    )
