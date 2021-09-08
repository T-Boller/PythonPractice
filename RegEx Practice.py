# Using a regex in Python, how can I verify that a user's password is:
# At least 8 characters
# Must be restricted to:
# uppercase letters: A-Z
# lowercase letters: a-z
# numbers: 0-9
# any of the special characters: @#$%^&+=
import re

for x in range(2):
    userPassword = input("""Please enter a password 
    This password must be between 8 and 16 characters long
    This password can contain uppercase and lower case letters, numbers, and characters '@#$%^&+='
    Password: """)
    validPass = re.match(r'^[a-zA-Z0-9@#$%^&+=]{8,16}$', userPassword)
    if validPass:
        print("Valid passowrd")
    else:
        print("Invalid pass")   

# Write a regex for a standard UK car license plate: 

for y in range(2):
    userLicense = input("Please enter your License plate: ")
    validLicense = re.match(r'^[A-Z]{2}[0-9]{2}\s?[A-Z]{3}$', userLicense)
    if validLicense:
        print("Valid License")
    else:
        print("Invalid License")   
 
# Write a regex for a a URL:

for z in range(2):
    userUrl = input("Please enter your URL: ")
    validUrl = re.match(r'^(www.)?[a-zA-Z0-9]+.[a-zA-Z.]{1,5}$', userUrl)
    if validUrl:
        print("Valid Url")
    else:
        print("Invalid Url")   


