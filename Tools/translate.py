'''
You can make mulitple line
comments using the three 's
you can also make single line comments using #
'''
def translate(phrase):
	translation = ""
	for letter in phrase:
		if letter in "AEIOUaeiou":
		# if letter.lower in "aeiou" 
			# if letter.isupper():
				#translation = translation + "Z"
			# else:
				# translation = translation + "z"
			translation = translation + "z"
		else:
			translation = translation + letter
	return translation

print(translate(input("enter a phrase: ")))