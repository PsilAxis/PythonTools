import secrets

import string

from datetime import datetime

# using the string module to define, letters, digits, and punctuation/special_chars
letters = string.ascii_letters
digits = string.digits

# Complete alphabet
alphabet = letters + digits

code_length = 4

while True:
    #Ask For new Password Length
    try:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        code_count = int(input("Number of Codes: "))
    #If there is an error
    except ValueError:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
        continue

    #Length input is valid
    else:
        #Length was successfully parsed!
        #we're ready to exit the loop.
        break

#Simple If & else for minimun int value.
if code_count >= 1:
	print ("Codes: " + str(code_count))
else:
	print ("Invalid")

#Generate X amount of Passwords
count = 0

#Time amd Date
currentTime = datetime.today().strftime('%Y-%m-%d %H:%M:%S ')
fileTime = currentTime.replace(":", ".")

#Create a new file and write the following line.
f = open(fileTime + "Codes.txt", "x")
f.write(currentTime + "\n" )

f.write("Generating ... " + str(code_count) + " Codes" + "\n" + "\n")


#run loop x amount of times. (x = pwd_count)
for i in range(code_count):

    #Each time the loop is ran add 1 to count.
    count += 1

    #Generate Password
    code1 = ''
    code2 = ''
    code3 = ''
    code4 = ''
    
    for i in range(code_length):

        #add new letter to current password.
        code1 += ''.join(secrets.choice(alphabet))

        code2 += ''.join(secrets.choice(alphabet))

        code3 += ''.join(secrets.choice(alphabet))

        code4 += ''.join(secrets.choice(alphabet))

        full_code = code1 + "-" + code2 + "-" + code3 + "-" + code4
    print(str(count) + ". " + str(full_code))
    #write passwords to file
    f = open(fileTime + "Codes.txt", "a")
    f.write(str(full_code + "\n" ))
    f.close()

    

