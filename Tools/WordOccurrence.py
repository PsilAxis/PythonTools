inFile = str(input('Please Input your file name and extension. (File.txt) \n'))
word = str(input('What word would you like to count?\n')).lower()

with open(inFile) as fl:
	data = fl.read()
	occurrences = data.lower().count(word)
	print(occurrences)
