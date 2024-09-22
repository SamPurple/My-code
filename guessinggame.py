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

	# answer = []
	# for i in range (0,4):
	# 	answer.append(random.choice(colours))
	# 	colours.remove(answer[i])

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



#	and guess2 == colour2 and guess3 == colour3 and guess4 == colour4:
#		win = True
#		print("WELL DONE YOU GUESSED IT!!!!!")
#	else:
#		if guess1 == colour1:


#answer = {'bead 1': colour1, 'bead 2': colour2, 'bead 3': colour3, 'bead 4': colour4 }

#guess = input(f"Topping {value} please: ")
#print(f"{pizza_toppings[0]}, {pizza_toppings[1]}, {pizza_toppings[2]}, {pizza_toppings[3]}, "
#	f"{pizza_toppings[4]}, {pizza_toppings[5]} and {pizza_toppings[6]}")

#unavailable_topping = random.choice(pizza_toppings)
#print(unavailable_topping)
#pizza_toppings.remove(unavailable_topping)

#print("\nHey Customer, tell me what pizza toppings you would like. You can choose 3.")

#pizza_order = []
#for value in range(1,4):
#	topping_choice = input(f"Topping {value} please: ")
#	while topping_choice not in pizza_toppings:
#		if topping_choice != unavailable_topping:
#			topping_choice = input(f"Sorry, {topping_choice} is not one of our toppings. Please choose another: ")
#		else:
#			topping_choice = input(f"Sorry, we have run out of {topping_choice}, please choose something else: ")
#	pizza_order.append(topping_choice)

#print("\nOk, making your pizza...")
#for pizza in pizza_order:
#	print(f"Adding {pizza}")


#input("\nYour pizza is ready!\nPress Enter to quit.")