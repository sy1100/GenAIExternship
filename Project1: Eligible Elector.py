# Step 1: age variable with user input.
age = int(input("How old are you? "))

# Step 2: if and elif loop to check eligibility with input age.
if age >= 18:
    print("Congratulations! You are eligible to vote. Go make a difference!")
elif age < 18:
    x = 18 - age # x calculate the difference between 18 and user input age.
    print("Oops! You're not eligible yet. But hey, only "+ str(x) +" more years to go!")
