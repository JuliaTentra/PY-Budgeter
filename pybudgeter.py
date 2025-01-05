import json
import os

class PyBudgeter:
    def __init__(self):
        self.data_file = "transactions.json"
        self.transactions = self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as file:
                return json.load(file)
        else:
            return []

    def save_data(self):
        with open(self.data_file, "w") as file:
            json.dump(self.transactions, file, indent=4)

    def add_transaction(self, amount, category, description):
        transaction = {
            "amount": amount,
            "category": category,
            "description": description
        }
        self.transactions.append(transaction)
        self.save_data()
        print(f"Transaction added: {amount} ({category}) - {description}")

    def view_summary(self):
        if not self.transactions:
            print("No transactions recorded yet.")
            return

        print("\nTransaction Summary:")
        total_income = sum(t['amount'] for t in self.transactions if t['amount'] > 0)
        total_expenses = sum(t['amount'] for t in self.transactions if t['amount'] < 0)
        print(f"  Total Income: ${total_income:.2f}")
        print(f"  Total Expenses: ${abs(total_expenses):.2f}")
        print(f"  Balance: ${total_income + total_expenses:.2f}")

        print("\nBy Category:")
        categories = {}
        for t in self.transactions:
            if t["category"] not in categories:
                categories[t["category"]] = 0
            categories[t["category"]] += t["amount"]

        for category, total in categories.items():
            print(f"  {category}: ${total:.2f}")

    def run(self):
        print("Welcome to PyBudgeter!")
        while True:
            print("\nWhat would you like to do?")
            print("1. Add a transaction")
            print("2. View summary")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                try:
                    amount = float(input("Enter amount (use negative for expenses): "))
                    category = input("Enter category (e.g., Food, Rent, Salary): ")
                    description = input("Enter description: ")
                    self.add_transaction(amount, category, description)
                except ValueError:
                    print("Invalid input. Please enter a valid number for the amount.")
            elif choice == "2":
                self.view_summary()
            elif choice == "3":
                print("Goodbye! Your data has been saved.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    budgeter = PyBudgeter()
    budgeter.run()
