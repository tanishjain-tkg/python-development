from decimal import Decimal, InvalidOperation

def add_expense(expenses):
    description = input("Enter description: ").strip()
    category = input("Enter category: ").strip()

    if not description or not category:
        print("Description and category cannot be empty.")
        return

    try:
        amount = Decimal(input("Enter amount: ").strip())
    except InvalidOperation:
        print("Invalid amount. Please enter a number.")
        return

    if not amount.is_finite() or amount <= 0:
        print("Amount must be a positive, finite number.")
        return

    expense = {
        "id": len(expenses) + 1,
        "description": description,
        "category": category,
        "amount": amount,
    }

    expenses.append(expense)
    print("Expense added successfully.")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    for expense in expenses:
        print(
            f"ID: {expense['id']} | "
            f"{expense['description']} | "
            f"{expense['category']} | "
            f"₹{expense['amount']:.2f}"
        )


def view_total(expenses):
    total = sum(
        (expense["amount"] for expense in expenses),
        start=Decimal("0"),
    )
    print(f"Total spending: ₹{total:.2f}")


def main():
    expenses = []

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add expense")
        print("2. View expenses")
        print("3. View total spending")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_total(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()