Arr = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 0] # the array you wish to extract numbers from
NewArr = [] # the new array that will recieve the extracted numbers.

def LessThan(Arr): # define a function called LessThan that uses Arr.
	for i in Arr: # run for each item(i) in the array
		if i <= 10: # if the i is less than or equal to 10. 
			NewArr.append(i) # add item to NewArr.
	print(Arr)
	print('All Numbers less than or equal to 10 \n', NewArr) # Make sure indentation is correct so it only runs once the loop is finished.

LessThan(Arr) #Run Function.
