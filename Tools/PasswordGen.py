#import secrets module to create an encrypted/hidden output. use import random for public outputs.
import secrets
#import string module to help create dictionary definition.
import string
#import so you can call time values.
from datetime import datetime

# using the string module to define, letters, digits, and punctuation/special_chars
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

# Complete alphabet
alphabet = letters + digits + special_chars

#Input Number of Passwords and handle errors
while True:
    #Ask For new Password Length
    try:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        pwd_count = int(input("Number of Passwords: "))
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

#Input Desired Password Length and handle errors
while True:
    #Ask For new Password Length
    try:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        pwd_length = int(input("Password Length: "))
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
if pwd_count >= 1:
	print ("Passwords: " + str(pwd_count))
else:
	print ("Invalid")

if pwd_length >= 1:
	print ("Length: " + str(pwd_length))
else:
	print ("Invalid")

#Generate X amount of Passwords
count = 0

#Time amd Date
currentTime = datetime.today().strftime('%Y-%m-%d %H:%M:%S ')
fileTime = currentTime.replace(":", ".")

#Create a new file and write the following line.
f = open(fileTime + "Passwords.txt", "x")
f.write(currentTime + "\n" )

f.write("Generating ... " + str(pwd_count) + " Passwords with " + str(pwd_length) +" Characters"+ "\n" + "\n" )



#run loop x amount of times. (x = pwd_count)
for i in range(pwd_count):

    #Each time the loop is ran add 1 to count.
    count += 1

    #Generate Password
    pwd = ''

    #Run loop for a random letter x times. x = pwd_length
    for i in range(pwd_length):

        #add new letter to current password.
        pwd += ''.join(secrets.choice(alphabet))
    #print the current count and password.
    print(str(count) + ".", pwd)

    #write passwords to file
    f = open(fileTime + "Passwords.txt", "a")
    f.write(str(count) + ". " + str(pwd + "\n" ))
