# Personal Budget Tracker

budget = {
    "food": [],
    "transportation": [],
    "entertainment": []
}

def add_expense(category, amount):
    if category in budget:
        budget[category].append(amount)
    else:
        print("Invalid category")

def view_budget():
    for category, expenses in budget.items():
        total = sum(expenses)
        print(f"{category.capitalize()}: ${total:.2f}")

add_expense("food", 25.50)
add_expense("entertainment", 50)
view_budget()
