class ExpenseTrackerError(Exception):
    """Base exception for the Expense Tracker application."""


class InvalidExpenseError(ExpenseTrackerError):
    """Raised when expense data is invalid."""


class ExpenseNotFoundError(ExpenseTrackerError):
    """Raised when an expense ID does not exist."""


class StorageError(ExpenseTrackerError):
    """Raised when expense data cannot be loaded or saved."""
