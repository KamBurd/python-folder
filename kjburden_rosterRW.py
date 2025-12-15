#  NCAT Kameron Burden
#  COMP-163 : Section 01
#  Instructor : Derrick Leflore
#  Description : Gives a list of options for a user to either create or print a roster, as well as edit an existing roster in a text file.
# naming convention : kjburden_rosterRW.py



#Function to show menu options regarding what to do with the text file
def showMenu():
    print("A) Create Roster")
    print("B) Print Roster")
    print("C) Edit Roster")
    print("Q) Exit")

#Function that allows the user to create a roster of names in a newly mad text file.

#The user can exit the prompt and return to the menu by entering the character 'x'.
def createRoster():
    roster= open("roster.txt", "w")
    print("")
    print("Enter roster name, x to quit")
    while True:
        name = input("Enter name : ")
        if name.upper() == "X":
            break
        roster.write(name+"\n")

#Function to display the roster of names previously entered by the user.
def printRoster():
    roster = open("roster.txt", "r")
    for i in roster:
        print(i)
    roster.close()


#Function that allows the user to edit the roster that they previously created by adding more names to it.

#The user can exit the prompt and return to the menu by entering the character 'x'
def editRoster():
    roster = open("roster.txt", "a")
    print("Enter a roster to add to the existing roster, x to quit")
    while True:
        name = input("Enter name : ")
        if name.upper() == "X":
            break
        roster.write(name+"\n")
    roster.close()
         
    

#The user will be prompted to choose a menu option from the displayed menu

#Entering the character 'q' will break the loop and print a goodbye message, ending the code.
while True:
    showMenu()
    option = input("Enter Menu Option : ").upper()
    if option == 'Q':
        break
    elif option == "A":
        createRoster()
    elif option == "B":
        printRoster()
    elif option == "C":
        editRoster()
    else:
        print("Invalid Option")

#Goodbye message
print("Good Bye!")
