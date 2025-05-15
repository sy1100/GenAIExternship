# Task 1
variable_string = "Python is amazing!"

print("First word: " + variable_string[:6])
print("Amazing part: " + variable_string[10:17])
print("Reversed string: " + variable_string[::-1])

# Task 2
variable_string_2 = " hello, python world! "
print(variable_string_2.strip())
print(variable_string_2.capitalize())
print(variable_string_2.replace("world","universe"))
print(variable_string_2.upper())

# Task 3
user_input = input("Enter a word: ")
palindrome = user_input[::-1]
if user_input == palindrome:
    print ("Yes, \'" + user_input + "\' is palindrome")
else:
    print ("No, \'" + user_input + "\' is not palindrome")
