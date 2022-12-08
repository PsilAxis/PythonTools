Array = [] # Create an array
Array = [1, 5, 8, 9, 7] # push numbers into array
print(Array)

x = len(Array) # find the Length of the array
print('Length of the array is ', x) # print the length


def _sum(Array): # define new function called _sum that will take in Array as the input
	sum = 0 # create varialble called sum, it starts at 0

	for i in Array: # run the loop for each object in the Array.
		sum = sum + i # sum equals sum + i. 
					  # adding to the total each time it loops.

	return(sum) # returns the sum of all the numbers together

ans = _sum(Array) #create variable ans and make it equal _sum(Array)
print('Sum of the array is ', ans)