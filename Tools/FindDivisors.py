while True: # While this is looping
	try: # try to get
		num = int(input("Please input number: ")) # Take user input as an integer and call it num1
	except ValueError: # if there is a ValueError(input invalid)
		print("Sorry, Please Input A Number.") # print error
		continue # Continue from the start of the loop
	else: # Otherwise if your input is correct
		break # break out of loop

divisorList = [] # create empty array

if num > 0:
	listRange = range(1,num+1) # create a positive range
	valid = True

elif num < 0:
	listRange = range(-1,num-1, -1) # create a negative range
	valid = True

else: # handle error/input of zero.
	valid = False

if valid == True:
	for number in listRange: # run loop for each number in range
			if num % number == 0: # check if num divided by number has a remainder of 0; modulo(%)
				divisorList.append(number) # add all valid numbers to divisor array.
	print(divisorList) #final outputs
	print("All these numbers are divisors of " + str(num))
else: # error output
	print('invalid')