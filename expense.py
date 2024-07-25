class Expense:

    def __init__(my, name, category, amount) -> None:
        my.name = name
        my.category = category
        my.amount = amount

    def __repr__(my):
        return f"<Expense: {my.name}, {my.category}, ₹{my.amount: .2f}>"