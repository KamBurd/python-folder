def showMenu():
    print("A) Create Roster")
    print("B) Print Roster")
    print("C) Edit Roster")
    print("Q) Exit")


def printRoster():
    roster = open("roster.txt", "r")
    for i in roster:
        print(i)
    roster.close()
def createRoster():
    roster= open("roster.txt", "w")
    print("")
    print("Enter roster name, x to quit")
    while True:
        name = input("Enter name : ")
        if name.upper() == "X":
            break
        roster.write(name+"\n")
def editRoster():
    roster = open("roster.txt", "a")
    print("Enter a roster to add to the existing roster, x to quit")
    while True:
        name = input("Enter name : ")
        if name.upper() == "X":
            break
        roster.write(name+"\n")
    roster.close()
         
    

       



    
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
print("Good Bye!")