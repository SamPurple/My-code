import random

pizza_toppings = ["chicken", "pepperoni", "mushrooms", "peppers", "pineapple", "ham", "spicy beef"]

print("Hi! Welcome to Sam's Pizzeria.  We make pizzas to order.  Our "
	"toppings are:")
print(f"{pizza_toppings[0]}, {pizza_toppings[1]}, {pizza_toppings[2]}, {pizza_toppings[3]}, "
	f"{pizza_toppings[4]}, {pizza_toppings[5]} and {pizza_toppings[6]}")

unavailable_topping = random.choice(pizza_toppings)
print(unavailable_topping)
pizza_toppings.remove(unavailable_topping)

print("\nHey Customer, tell me what pizza toppings you would like. You can choose 3.")

pizza_order = []
for value in range(1,4):
	topping_choice = input(f"Topping {value} please: ")
	while topping_choice not in pizza_toppings:
		if topping_choice != unavailable_topping:
			topping_choice = input(f"Sorry, {topping_choice} is not one of our toppings. Please choose another: ")
		else:
			topping_choice = input(f"Sorry, we have run out of {topping_choice}, please choose something else: ")
	pizza_order.append(topping_choice)

print("\nOk, making your pizza...")
for pizza in pizza_order:
	print(f"Adding {pizza}")


input("\nYour pizza is ready!\nPress Enter to quit.")