def isPalindrome(i): # create a function to check if string isPalindrome or not.
	return i == i[::-1] # Check if i equalt i backwards. i[::-1] Start at the end of the string and read backwards

i = str(input("Please input a word: ")) # ask for user input of a string
ans = isPalindrome(i) # run the function using the string and get the answer, Yes or no.

if ans: # if it is a palindrome
	print("Yes")
else: # otherwise 
	print("No")