# Step 1
password = input("Enter your password: ")
error_list = []
score = 0

# Step 2

#length
if len(password) < 8:
    error_list.append("8 characters")
else:
    score += 2
#upper
if any(password.find(upper) > -1 for upper in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    score += 2
else:
    error_list.append("one upper case")
#lower
if any(password.find(lower) > -1 for lower in "abcdefghijklmnopqrstuvwxyz"):
    score += 2
else:
    error_list.append("one lower case")
#digit
if any(password.find(digits) > -1 for digits in "0123456789"):
    score += 2
else:
    error_list.append("one digit")

#special character
if any(password.find(special) > -1 for special in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"):
    score += 2
else:
    error_list.append("one special character")

if not error_list:
    print("Your password is strong! 💪" + "Your password score is " + str(score) + ".")

else:
    print("Your password needs at least " + " and ". join(error_list) + ". Your password score is " + str(score) + ".")






