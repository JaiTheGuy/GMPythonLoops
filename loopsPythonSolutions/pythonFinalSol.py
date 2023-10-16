# Goal: Create a game where you keep guessing a number until you get it right!
# Step 1: Create a variable that holds onto a random number based on your preferred range (hint: you might need to import!).
# Step 2: Make a while loop where the condition is 'True'.
# Step 3: Have the user guess the number and each time they guess incorrectly, have a print statement that tell them to keep guessing.
# Step 4: If they guess the number correctly, use a print statement to congradlate them and then break from the loop.

# BONUS:
#1: Tell the user if their guess is higher or lower after each turn.
#2: Tell user how many turns it took them to get the answer right when they win.
#3:  If someone enters something that's not a number or a number out of the range, have a condition that prints out an error message for that turn and ask them to try again.

########### CODE BELOW HERE #########

import random

answer = random.randint(1, 10)

print("Welcome to the Number Guessing Game!")
print("Numbers go from 1 - 10")


while True:
		guess = int(input("Enter your guess: "))
		if guess == answer:
				print("Congratulations! You guessed the number", guess,"!")
				break
		else: 
			print("Keep on guessing")










