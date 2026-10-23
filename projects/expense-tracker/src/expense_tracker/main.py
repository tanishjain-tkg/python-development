import logging
from pathlib import Path

from .exceptions import (
    ExpenseNotFoundError,
    InvalidExpenseError,
    StorageError,
)

from .services import (
    add_expense,
    calculate_total,
    delete_expense,
    list_expenses,
)

from .storage import load_expenses, save_expenses

def configure_logging():
    log_dir = Path(__file__).resolve().parents[2] / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        filename=log_dir / "expense_tracker.log",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        encoding="utf-8",
    )

logger = logging.getLogger(__name__)

def display_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    for expense in list_expenses(expenses):
        print(
            f"ID: {expense.id} | "
            f"{expense.description} | "
            f"{expense.category} | "
            f"₹{expense.amount:.2f} | "
            f"{expense.date}"
        )

def prompt(message):
    value = input(message).strip()

    if value.lower() == ":q":
        raise SystemExit

    return value

def main():
    configure_logging()
    logger.info("Expense Tracker started.")

    try:
        expenses = load_expenses()
    except StorageError as exc:
        logger.error("Could not initialize application: %s", exc)
        print(f"Error loading expenses: {exc}")
        return

    print(f"Loaded {len(expenses)} expense(s).")
    print("Enter ':q' at any prompt to exit.")

    try:
        while True:
            print("\n=== Expense Tracker ===")
            print("1. Add expense")
            print("2. View expenses")
            print("3. View total spending")
            print("4. Delete expense")
            print("5. Exit")

            choice = prompt("Choose an option: ")

            if choice == "1":
                description = prompt("Enter description: ")
                category = prompt("Enter category: ")
                amount_input = prompt("Enter amount: ")

                try:
                    expense = add_expense(
                        expenses,
                        description,
                        category,
                        amount_input,
                    )
                    save_expenses(expenses)
                    print(f"Expense {expense.id} added successfully.")

                except InvalidExpenseError as exc:
                    print(f"Could not add expense: {exc}")
                except StorageError as exc:
                    print(f"Could not save expense: {exc}")

            elif choice == "2":
                display_expenses(list_expenses(expenses))

            elif choice == "3":
                print(f"Total spending: ₹{calculate_total(expenses):.2f}")

            elif choice == "4":
                if not expenses:
                    print("No expenses available to delete.")
                    continue

                display_expenses(expenses)

                try:
                    expense_id = int(
                        prompt("Enter the expense ID to delete: ")
                    )
                except ValueError:
                    print("Expense ID must be an integer.")
                    continue

                confirmation = prompt(
                    f"Delete expense {expense_id}? (y/n): "
                ).lower()

                if confirmation != "y":
                    print("Deletion cancelled.")
                    continue

                try:
                    deleted = delete_expense(expenses, expense_id)
                    save_expenses(expenses)
                    print(f"Deleted expense {deleted.id}.")
                except ExpenseNotFoundError as exc:
                    print(exc)
                except StorageError as exc:
                    print(f"Could not save deletion: {exc}")

            elif choice == "5":
                break

            else:
                print("Invalid choice. Please select 1–5.")

    except (SystemExit, KeyboardInterrupt):
        print("\nExiting Expense Tracker.")

    finally:
        logger.info("Expense Tracker stopped.")

    print("Goodbye!")



if __name__ == "__main__":
    main()
