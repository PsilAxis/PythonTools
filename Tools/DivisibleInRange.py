# Create a range and pick a divider. Will output numbers within the range that are divisible by the number.
# I.E. range 1 - 10 with divider of 3 will show [3, 6, 9]

while True: # While this is looping
	try: # try to get
		num1 = int(input("Range starting number: ")) # Take user input as an integer and call it num1
	except ValueError: # if there is a ValueError(input invalid)
		print("Sorry, Please Input A Number.") # print error
		continue # Continue from the start of the loop
	else: # Otherwise if your input is correct
		break # break out of loop

while True: # While this is looping
	try: # try to get
		num2 = int(input("Range ending number: ")) # Take user input as an integer and call it num2
	except ValueError: # if there is a ValueError(input invalid)
		print("Sorry, Please Input A Number.") # print error
		continue # Continue to from the start of the loop
	else: # Otherwise if your input is correct
		break # break out of loop

##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################

if num1 == num2: # if numbers are the same, return error.
	print("Invalid range from " + str(num1) + " to " + str(num2))

elif num1 > num2: # if num1 is less than num2
	Range = range(num1,num2-1, -1) # Create a Range from the two numbers. 100, 1 shows `100-2' so we use num2-1 to get 100-1.
	print("You chose a range from " + str(num1) + " to " + str(num2))
	
	while True: # While this is looping
		try: # try to get
			divi = int(input("Enter a Divider: ")) # Take user input as an integer and call it divi
		except ValueError: # if there is a ValueError(input invalid)
			print("Sorry, Please Input A Number.") # print error
			continue # Continue to from the start of the loop
		else: # Otherwise if your input is correct
			break # break out of loop

	New = [] # Create New Array

	for i in Range: # run loop for each item(i) in Range
		result = i % divi # i modulo(%) divi;(number divided by divi, check for remainder.)
		if result == 0: # if the remainder is 0.
			New.append(i) #Add number to the list
	print(New) #Print the New array once the loop is finished running.

else: # Else, the only valid option is |if num2 less than num1|
	Range = range(num1,num2+1) # Create a Range from the two numbers. 1,100 shows `1-99' so we use num2+1 to get '1-100'.
	print("You chose a range from " + str(num1) + " to " + str(num2))
	
	while True: # While this is looping
		try: # try to get
			divi = int(input("Enter a Divider: ")) # Take user input as an integer and call it divi
		except ValueError: # if there is a ValueError(input invalid)
			print("Sorry, Please Input A Number.") # print error
			continue # Continue to from the start of the loop
		else: # Otherwise if your input is correct
			break # break out of loop
				
	New = [] # Create New Array

	for i in Range: # run loop for each item(i) in Range
		result = i % divi # i modulo(%) divi;(number divided by divi, check for remainder.)
		if result == 0: # if the remainder is 0.
			New.append(i) #Add number to the list

	print(New) #Once the loop is finished running, Print the New array with all the numbers divisible by divi.
	print('All these numbers are divisible by ' + str(divi))