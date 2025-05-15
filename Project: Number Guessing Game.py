# Step 1
import random
number_to_guess = random.randint(1, 100)
print(number_to_guess)
user_guess = int(input("Guess a number (between 1 and 100): "))
attempts = 1

# Step 2
while attempts <= 10:
    if user_guess == number_to_guess:
        print ("Congratulations! You guessed it in " + str(attempts) + " attempts!")
        break
    elif user_guess > number_to_guess:
        print ("Too high! Try again.")
        attempts += 1
    elif user_guess < number_to_guess:
        print ("Too low! Try again.")
        attempts += 1

    if attempts > 10:
        print ("Game over! Better luck next time!")
        break
    else:
        user_guess = int(input("Guess a number (between 1 and 100): "))





