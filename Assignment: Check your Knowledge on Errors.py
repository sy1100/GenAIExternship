# Task 1
user_input =int(input("Enter a number: "))
try:
    result = 100/user_input
except ZeroDivisionError:
    print("Oops! You cannot divide by zero.")
except ValueError:
    print("Invalid input!")
else:
    print("100 divided by " + str(user_input) + " is " + str(result))

# Task 2
my_list = [1,2,3,4,5]
try:
    print(my_list[7])
except IndexError:
    print("IndexError occurred! List index out of range.")

my_dictionary = {"name": "Alice"}
try: print(my_dictionary["age"])
except KeyError:
    print("KeyError occurred! Key not found in the dictionary.")

try:
    "Hello" + 5
except TypeError:
    print("TypeError occurred! Unsupported operand types.")

#Task 3
first_input = int(input("Enter the first number: "))
second_input = int(input("Enter the second number: "))

try:
    result = first_input/second_input
except ZeroDivisionError:
    print("Oops! You cannot divide by zero.")
except ValueError:
    print("Invalid input!")
else:
    print("The result is " + str(result)+ ".")
finally:
    print("This block always executes.")
