# Task 1
starting_number = int(input("Enter the starting number: "))

while starting_number != 0:
    print(starting_number, end = " ")
    starting_number -= 1
print ("Blast off🚀")

# Task 2
user_input = int(input("Enter a number:"))
for i in range(1,11):
    result = user_input * i
    print(str(user_input)+" x "+ str(i)+ " = "+str(result), end= " ")

# Task 3
user_input = int(input("Enter a number:"))
result = 1
for i in range (1,user_input+1):
    result *= i
print("The factorial of " + str(user_input) + " is " + str(result) + ".")