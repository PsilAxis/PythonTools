while True:
	try:
		i = int(input("Enter a number: ")) # Take user input and call it i
	except ValueError:
		print("Sorry, Please Input A Number.")
		continue
	else:
		break;

if i % 3 == 0 and i % 5 == 0: 
# i divided by 3, i divided by 5, if the REMAINDER(%) of both the operations IS EQUAL TO(==) 0
	print('FIZZBUZZ')
	print(str(i) + ' is divisible by both 3 and 5')

elif i % 5 == 0: 
# i is divided by 5 if the REMAINDER(%) IS EQUAL TO(==) 0
	print('BUZZ')
	print(str(i) + ' is divisible by 5')

elif i % 3 == 0: 
# i is divided by 3 if the REMAINDER(%) IS EQUAL TO(==) 0
	print('FIZZ')
	print(str(i) + ' is divisible by 3')

else: 
# none of the above.
	print(str(i) + 'is neither fizz nor buzz');