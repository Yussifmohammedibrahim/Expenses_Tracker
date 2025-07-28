def main():
    expenses = []
    load_expenses(expenses)
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. Show Expense Summary")
        print("4. Save and Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_summary(expenses)
        elif choice == "4":
            save_expenses(expenses)
            print("\nGoodbye! Your expenses have been saved.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def add_expense(expenses):
    print("\nAdd New Expense")
    while True:
        try:
            amount = float(input("Enter amount spent: $"))
            if amount <= 0:
                print("Amount must be positive. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")
    
    category = input("Enter category (e.g., Food, Transport, Entertainment): ").strip().title()
    description = input("Enter description: ").strip()
    
    expense = {
        'amount': amount,
        'category': category,
        'description': description
    }
    
    expenses.append(expense)
    print(f"Expense of ${amount:.2f} for {category} added successfully!")

def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses recorded yet.")
        return
    
    print("\nAll Expenses:")
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. ${expense['amount']:.2f} - {expense['category']} - {expense['description']}")

def show_summary(expenses):
    if not expenses:
        print("\nNo expenses recorded yet.")
        return
    
    summary = {}
    for expense in expenses:
        category = expense['category']
        summary[category] = summary.get(category, 0) + expense['amount']
    
    print("\nExpense Summary by Category:")
    for category, total in summary.items():
        print(f"- {category}: ${total:.2f}")

def save_expenses(expenses):
    with open("expenses.txt", "w") as file:
        for expense in expenses:
            line = f"{expense['amount']},{expense['category']},{expense['description']}\n"
            file.write(line)

def load_expenses(expenses):
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    try:
                        expense = {
                            'amount': float(parts[0]),
                            'category': parts[1],
                            'description': parts[2]
                        }
                        expenses.append(expense)
                    except ValueError:
                        continue
    except FileNotFoundError:
        pass  # First run, file doesn't exist yet

if __name__ == "__main__":
    main()