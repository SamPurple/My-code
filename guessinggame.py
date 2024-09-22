import random

play_again = 'y'

while play_again == 'y':

	colours = ["red", "blue", "green", "orange", "yellow", "silver", "gold"]

	print("Hi! Welcome to Sam's Guessing Game.  I've got 4 different coloured beads in a line.  You need to guess the colours and the order. ")
	print("\nPossible bead colours are red, blue, green, orange, yellow, silver and gold. ")
	duplicate = input("\nDo you want to play with duplicate colours? Enter y or n: ")
	print("\nOK, time to guess those beads!!!\n")

	colour1 = random.choice(colours)
	if duplicate == 'n':
		colours.remove(colour1)
	colour2 = random.choice(colours)
	if duplicate == 'n':
		colours.remove(colour2)
	colour3 = random.choice(colours)
	if duplicate == 'n':
		colours.remove(colour3)
	colour4 = random.choice(colours)
	if duplicate == 'n':
		colours.remove(colour4)

	answer = [colour1, colour2, colour3, colour4]

	win = False
	number_of_guesses = 0

	while win == False:
		
		right_in_right_place = 0
		right_in_wrong_place = 0
		answer_remainder = [colour1, colour2, colour3, colour4]
		guess1 = input("Bead 1: ")
		if guess1 == colour1: 
			right_in_right_place = right_in_right_place + 1
			answer_remainder.remove(colour1)
		guess2 = input("Bead 2: ")
		if guess2 == colour2: 
			right_in_right_place = right_in_right_place + 1
			answer_remainder.remove(colour2)
		guess3 = input("Bead 3: ")
		if guess3 == colour3: 
			right_in_right_place = right_in_right_place + 1
			answer_remainder.remove(colour3)
		guess4 = input("Bead 4: ")
		if guess4 == colour4: 
			right_in_right_place = right_in_right_place + 1
			answer_remainder.remove(colour4)

		number_of_guesses = number_of_guesses + 1

		if right_in_right_place == 4:
			print("\nW E L L     D O N E !!!!")
			print("\nYOU GUESSSED CORRECTLY!!!")
			print("\nY O U    W I N !!!!")
			print(f"\nYou did it in {number_of_guesses} guesses!")
			win = True

		else:	
			if guess1 != colour1 and guess1 in answer_remainder: 
				right_in_wrong_place = right_in_wrong_place + 1
				answer_remainder.remove(guess1)

			if guess2 != colour2 and guess2 in answer_remainder: 
				right_in_wrong_place = right_in_wrong_place + 1
				answer_remainder.remove(guess2)

			if guess3 != colour3 and guess3 in answer_remainder: 
				right_in_wrong_place = right_in_wrong_place + 1
				answer_remainder.remove(guess3)

			if guess4 != colour4 and guess4 in answer_remainder: 
				right_in_wrong_place = right_in_wrong_place + 1
				answer_remainder.remove(guess4)
	
		print(f"\nYou have guessed: \n{right_in_right_place} RIGHT in the RIGHT place.")
		print(f"And: \n{right_in_wrong_place} RIGHT in the WRONG place\n")

	print("Press 'y' to play again or enter to quit")
	play_again = input()
