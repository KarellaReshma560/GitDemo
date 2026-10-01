
import random
print("Welcome to the Number Guessing Game.")
print("You have to guess the number between 1 and 50. You have only 5 chances to guess it.")
num = random.randint(1, 50)
max_attempt = 5
counter = 0
is_guess_correct = False

while counter < max_attempt:
    guess = int(input("Guess the number: "))
    if guess == num:
        print("You have guessed correct number")
        is_guess_correct = True
        break
    else:
        if guess < num:
            higher_or_lower = "Higher"
        else:
            higher_or_lower = "Lower"
    print(f"Your guess is wrong! Try {higher_or_lower} number.")

    counter += 1
if not is_guess_correct:
    print("Bad luck !!. You have not guessed the correct number.")
print("Game Over!!. Thank you for playing")

