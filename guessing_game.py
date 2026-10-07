import random

secret_number = random.randint(1, 20)
attempts = 0

print("--- Welcome to the Guessing Game with Score Tracker! ---")
print("I'm thinking of a number between 1 and 20.")

while True:
    user_guess = int(input("Take a guess: "))
    attempts = attempts + 1
    
    if user_guess < secret_number:
        print("Too low! Try a higher number.")
    elif user_guess > secret_number:
        print("Too high! Try a lower number.")
    else:
        print(f"🎉 Congratulations! You guessed the correct number!")
        print(f"🏆 Total Attempts: {attempts}")
        break
