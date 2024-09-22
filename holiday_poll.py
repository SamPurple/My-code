poll_results = {}

while True:
	name = input("What is your name? ")
	response = input("\nWhere would you most like to go on holiday? ")

	poll_results[name] = response
	# this stores the info in the dictionary!

	repeat = input("\nWould you like to let another person respond? (y/n) ")
	if repeat == 'y':
		print('\n')
	else:
		break

print('\n---POLL RESULTS---')
for name, response in poll_results.items():
	print(f"{name.title()} would like to go on holiday to {response.title()}")

input('Press Enter to quit' )