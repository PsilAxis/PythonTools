while True: # While this is looping
	try: # try to 
		num = int(input("Enter a number: ")) # Take user input as an integer and call it num
	except ValueError: # if there is a ValueError(input invalid)
		print("Sorry, Please Input A Number.") # print error
		continue # Continue to from the start of the loop
	else: # Otherwise if your input is correct
		break # break out of loop

def OddEven(num): # Define a function called OddEven that takes in the num value.
	if num % 2 == 0:
		print("The Number " + str(num) + " is Even")
	else:
		print("The Number " + str(num) + " is Odd")

OddEven(num) # Run function