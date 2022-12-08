# Turn File into Array, Each line in the file is a new index
def read_file(filename):               #create new function
    array = []                         #create empty array
    with open(filename, 'r') as f:     # Open and Read file and call it f
        for line in f:                 # repeat for each line in f
            array.append(line.strip()) # add line contents to the array
    return array                       # Give full array of values

RedCode = input("Insert Your Code: ")  # Prompt User Input.

ValCode = 'ValidCode.txt'              # name of the valid code file.
ValidCodes = read_file(ValCode)        # Read the file as an array.
RemCodes = open('RemovedCodes.txt', 'a+')  # Open/Create RemovedCodes (RemCodes.txt) File.

if RedCode in ValidCodes:              # if the user input code is found in the valid codes file.

    with open(ValCode , 'r') as f:     # open ValCode as f.
        Read = f.readlines()           # read all lines. 
                                       
    with open(ValCode , 'w') as f:     #open and write
                                       
        for line in Read:              # check each line in Read.
            if line.strip('\n') != str(RedCode): # if contents of the line do not equal the contents of RedCode
                f.write(line)          # rewrite remaining valid codes into document.

    # Write the contents of RedCode into RemovedCodes.txt
    # remove(replace) unneeded special characters
    RemCodes.write(str(RedCode).replace(']', '').replace('[', '').replace('\'', '').replace('\"', '').replace(',', '').replace(' ', '') + "\n")

    print("Congratulations!")
    print("Code: " + str(RedCode))
    print("Has Been Redeemed Successfully!")
    RemCodes.close()

else:
    #print false if code is invalid

    print("Fail")
    print("Fail")
    print("Fail")
