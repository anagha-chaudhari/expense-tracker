from expense import Expense


def main():
    print(f"Running Expense Tracker")
    file_path = "expense.csv"

    # Get user to input for expense
    expense = get_expense()

    # Write theri expense to a file
    save_expense(expense, file_path)

    # Read file and summarize all expenses
    summarize_expense(file_path)
  

def get_expense():
    print(f"Getting User Expense")
    expenseName = input("Enter expense name: ")
    expenseAmt = float(input("Enter expense amount: "))
    print(f"You've entered {expenseName}, {expenseAmt}")

    expenseCategories = [
        "Food", 
        "Home", 
        "Work", 
        "Fun", 
        "Miscellaneous"
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expenseCategories):
            print(f"{i+1}. {category_name}")

        value = f"[1 - {len(expenseCategories)}]"
        index = int(input(f"Enter a category number {value}: ")) - 1
        
        if index in range(len(expenseCategories)):
            selectedCategory = expenseCategories[index]
            newExpense = Expense(name=expenseName, category=selectedCategory, amount=expenseAmt)

            return newExpense
                                 
        else:
            print("Invalid Category. Please try again!")

def save_expense(expense, file_path):
    print(f"Saving User Expense: {expense} to {file_path}")
    with open(file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense}\n")
   

def summarize_expense(file_path):
    print(f"Summarize User Expense")
   

if __name__ == "__main__":
    main()