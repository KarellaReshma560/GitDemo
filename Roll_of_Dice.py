""""
write a program to simulate a roll of dice.
The program should generate random numbers from 1 to 6

"""
import random

print("Welcome to the game of Rolling the Dice")

while True:
    choice = input("Press 'Enter' to roll the dice or q to 'quit.' ")
    choice = choice.strip()
    if choice == 'q':
        print("Thank you for playing, Bye!!")
        break
    elif choice == '':
        num = random.randint(1, 6)
        print(f"Your number is : {num}")
    else:
        print("Invalid Input!!")

print("GAME OVER")





