print ("Welcome to the Error-Free Calulator! Choose an operation:")
def main():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    user_input = int(input("> "))
    if user_input == 1:
        addition()
    elif user_input == 2:
        subtraction()
    elif user_input == 3:
        multiplication()
    elif user_input == 4:
        division()
    elif user_input == 5:
        return

def addition():
    try:
        first_num = int(input("Enter first number: "))

    except ValueError:
        print("Invalid input! Please enter a valid number.")
        logging.error("Invalid input! Please enter a valid number.")
        first_num = int(input("Re-Enter first number: "))

    try:
        second_num = int(input("Enter second number: "))
        print("The sum is:", first_num + second_num)
        return main()

    except ValueError:
        print("Invalid input! Please enter a valid number.")
        logging.error("Invalid input! Please enter a valid number.")
        return main()

def subtraction():
    try:
        first_num = int(input("Enter first number: "))

    except ValueError:
        print("Invalid input! Please enter a valid number.")
        logging.error("Invalid input! Please enter a valid number.")
        first_num = int(input("Re-Enter first number: "))

    try:
        second_num = int(input("Enter second number: "))
        print("The subtraction is:", first_num - second_num)
        return main()

    except ValueError:
        print("Invalid input! Please enter a valid number.")
        logging.error("Invalid input! Please enter a valid number.")

def multiplication():
    try:
        first_num = int(input("Enter first number: "))

    except ValueError:
        print("Invalid input! Please enter a valid number.")
        logging.error("Invalid input! Please enter a valid number.")
        first_num = int(input("Re-Enter first number: "))

    try:
        second_num = int(input("Enter second number: "))
        print("The multiplication is:", first_num * second_num)
        return main()

    except ValueError:
        print("Invalid input! Please enter a valid number.")
        logging.error("Invalid input! Please enter a valid number.")

def division():
    try:
        first_num = int(input("Enter first number: "))

    except ValueError:
        print("Invalid input! Please enter a valid number.")
        logging.error("Invalid input! Please enter a valid number.")
        first_num = int(input("Re-Enter first number: "))

    except ZeroDivisionError:
        print("Oops! Division by zero is not allowed.")
        logging.error("Oops! Division by zero is not allowed.")
        first_num = int(input("Re-Enter first number: "))
    try:
        second_num = int(input("Enter second number: "))
        print("The multiplication is:", first_num / second_num)
        return main()

    except ValueError:
        print("Invalid input! Please enter a valid number.")
        logging.error("Invalid input! Please enter a valid number.")
        return main()

    except ZeroDivisionError:
        print("Oops! Division by zero is not allowed.")
        logging.error("Oops! Division by zero is not allowed.")
        return main()

if __name__ == '__main__':
    import logging
    logging.basicConfig(
        filename='error_log.txt',
        level=logging.ERROR,
    )
    main()

