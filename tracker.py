import calendar
import datetime
from typing import List
from expense import Expense
from tabulate import tabulate

def main():
    print(green("🍀 The Expense Tracker!"))
    expense_file_path = "expense.csv" # setting a path where expense data will be saved
    budget_limit = 100000

    user_expense = get_user_expense() # calling fxn for getting user expenses

    write_expense_to_file(user_expense, expense_file_path) # calling fxn to save user's expense data to csv file

    summarize_expenses(expense_file_path, budget_limit) #calling fxn to summarize expenses from file

def get_user_expense() -> Expense: # defining get_user_expense fxn and returns Expense object
    print(yellow("💰 Your Expense"))
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    expense_categories = ["Food", "Home", "Work", "Shop", "Pet", "Fun", "Random"]

    while True: # starting infinite loop to make sure that user selects valid category
        print("Select a category: ")
        for index, category_name in enumerate(expense_categories): # enumerate to keep track of index and item itself
            print(green(f"  {index + 1}. {category_name}"))

        selected_index = int(input(f"Enter a category number [1 - {len(expense_categories)}]: ")) - 1

        if 0 <= selected_index < len(expense_categories):
            selected_category = expense_categories[selected_index]
            return Expense(name=expense_name, category=selected_category, amount=expense_amount)
        else:
            print(red("Invalid category. Please try again!"))

def write_expense_to_file(expense: Expense, file_path: str):
    print(yellow(f"💰 Saving Your Expense: {expense} to {file_path}"))
    try: # to handle potential errors
        with open(file_path, "a", encoding="utf-8") as file: # opening a file in append mode "a" with utf-8 encoding
            file.write(f"{expense.name},{expense.amount},{expense.category}\n") # writing expense details into the file
    except Exception as error:  # catches exceptions if occured during file operations
        print(red(f"Error writing to file: {error}")) 

def summarize_expenses(file_path: str, budget: float):
    print(yellow("/n /n💰 Summarizing Your Expenses"))
    expenses: List[Expense] = [] # initializing empty list to store class Expense objects
    try:  # to handle errors
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    name, amount, category = parts
                    expenses.append(Expense(name=name, amount=float(amount), category=category))
                else:
                    print(red(f"Skipping invalid line: {line.strip()}"))
    except Exception as error:
        print(red(f"Error reading from file: {error}"))
        return

    expenses_by_category = {}  # initializing empty dictionary to store total expenses by category
    for expense in expenses:
        expenses_by_category[expense.category] = expenses_by_category.get(expense.category, 0) + expense.amount

    table = [["Category", "Amount"]]  # want output in table format
    for category, amount in expenses_by_category.items():
        table.append([category, f"₹{amount:.2f}"])

    print(green("\n💵 Expenses By Category 💵:"))
    print(tabulate(table, headers="firstrow", tablefmt="grid")) # printing table using tabulate function

    total_expense = sum(expense.amount for expense in expenses)
    remaining_budget = budget - total_expense

    summary_table = [
        ["Total Spent", f"₹{total_expense:.2f}"],
        ["Budget Remaining", f"₹{remaining_budget:.2f}"]
    ]

    current_date = datetime.datetime.now() # current date and time
    days_in_month = calendar.monthrange(current_date.year, current_date.month)[1] # no of days in current month
    remaining_days = days_in_month - current_date.day 

    daily_budget = remaining_budget / remaining_days if remaining_days > 0 else 0
    summary_table.append(["Budget Per Day", green(f"₹{daily_budget:.2f}")])

    print(yellow("\nSummary:"))
    if remaining_budget <= 0:
        summary_table.append([red("No balance left"), red("0.000")])
    print(tabulate(summary_table, tablefmt="grid"))

    # colour functions with ANSI escape codes

def green(text: str) -> str:
    return f"\033[92m{text}\033[0m"

def red(text: str) -> str:
    return f"\033[91m{text}\033[0m"

def yellow(text: str) -> str:
    return f"\033[93m{text}\033[0m"


if __name__ == "__main__":
    main()
