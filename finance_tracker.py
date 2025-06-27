print("Welcome to the Personal Finance Tracker!")

my_expenses = {}

def add_expenses(data):
    try:
        user_description = input("Enter description: ")
        user_category = input("Enter category: ")
        user_amount = float(input("Enter amount: "))

        if user_category not in data:
            data[user_category] = []

        data[user_category].append((user_description, user_amount))
        print("Expense added successfully.\n")

    except ValueError:
        print("Invalid input\n")


def view_expenses(data):
    if not data:
        print("No expenses")
        return

    for key, value in data.items():
        print(f"Category:{key}")
        for description, amount in value:
            print(f" - {description}: $ {amount:.2f}")


def view_summary(data):
    if not data:
        print("No expenses")
        return
    print("Summary:")
    for category, items in data.items():
        total = 0
        for item in items:
            total += item[1]
        print(f"{category}: ${total:.2f}")

def main():
    while True:
        print("What would you like to do?")
        print ("1. Add Expense")
        print ("2. View All Expense")
        print ("3. View Summary")
        print ("4. Exit")
        user_input = int(input("Choose an option: "))

        if user_input == 1:
            add_expenses(my_expenses)
        elif user_input == 2:
            view_expenses(my_expenses)
        elif user_input == 3:
            view_summary(my_expenses)
        elif user_input == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid input\n")

if __name__ == "__main__":
    main()
    


    


