import turtle

# Function for factorial
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# Function for fibonacci
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

# Fractal tree setting
def tree_setup():
    global t
    t = turtle.Turtle()
    t.reset()
    t.speed(6)
    t.color("black")
    t.left(90)
    t.up()
    t.backward(100)
    t.down()

# Function for fractal tree
def fractal(length, depth=0):
    if depth <4:
        depth += 1
        next_length = length *(0.7 ** depth)
        t.forward(length)
        t.left(60)
        fractal(next_length, depth)
        t.right(30)
        fractal(next_length, depth)
        t.right(30)
        fractal(next_length, depth)
        t.right(30)
        fractal(next_length, depth)
        t.right(30)
        fractal(next_length, depth)
        t.left(60)
        t.backward(length)

# Function for menu selection
def main():
    print("Welcome to the Recursive Artistry Program"
          "\nChoose an option:"
          "\n1. Calculate Factorial"
          "\n2. Find Fibonacci"
          "\n3. Draw a Recursive Fractal"
          "\n4. Exit")
    user_input = int(input("> "))

    if user_input == 1:
        num = int(input("Enter a number to find its factorial: "))
        print("\nFactorial of " + str(num) + " is", factorial(num),"\n")
        return main()

    elif user_input == 2:
        num = int(input("Enter a number to find its Fibonacci: "))
        print( "The " + str(num) +"th Fibonacci number is", fibonacci(num),"\n")
        return main()


    elif user_input == 3:
        print("A simple fractal tree drawing! 🌳\n")
        tree_setup()
        fractal(100)
        turtle.done()
        return main()

    elif user_input == 4:
        exit()

# call main function
main()

