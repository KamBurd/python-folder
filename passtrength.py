#Kameron Burden
#4/5/2023
#Lab 2 Strong password checker
import re

#Password checking function
def checkpass(passwo):
    #Checks if password length is at least 8
    if len(passw) < 8: 
        return "Weak Password"
    #Checks if password has captial letter
    if not re.search(r'[A-Z]', passwo):
        return "Weak Password"
    #Checks if password has lowercase letter
    if not re.search(r'[a-z]', passwo):
        return "Weak Password"
    #Checks if password has numbers
    if not re.search(r'\d', passwo):
        return "Weak Password"
    #Checks if password has a special character
    if not re.search(r'[!@#$%^&*()_+=-]', passwo):
        return "Weak Password"
    #If the password passes all the conditions, its a strong password
    return "Strong Password"
    
    
passw = input("Enter password: ")
print(checkpass(passw))

    

    
