#Name: Kameron Burden
#Date: 9/25/2022
#Class: COMP163001.202310
#This program is meant to prompt the user for 2 numbers, then have the user choose which operation the numbers will use.


#The starting menu that explains what happens in the code.
def printHeader():
    print("Welcome to Aggie Calculation, enter 2 numbers and choose what operation they get.")
    print("================================================================================")
    print('\n')

#The menu that explains the choices to the user.
def menu():
    print("Choose which operation the numbers should do. The choices are:")
    print("Addition + (Enter 1)")
    print("Subtraction - (Enter 2)")
    print("Multiplication * (Enter 3)")
    print("Division / (Enter 4)")
    print("==============================================================")
    print("\n")
printHeader()
#The prompts that ask the user for 2 numbers
num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number "))
print("\n")

menu()
#The prompt that asks the user which operation they would want to use.
choice = int(input("Choose which operation the first and second number will use. "))


#The 4 functions that are meant to return the value of the two numbers depending on the chosen operation
def add(x, y):
    z = x + y
    return z

def sub(x, y):
    z = x - y
    return z

def mult(x, y):
    z = x * y
    return z

def div(x, y):
    z = x / y
    return z

#The answer is printed out. The user is then asked if they would like to continue the code.
#If the answer is yes, the menus will reappear and prompt the user for another set of numbers and another choice of operation.
#If the answer is no, the loop is broken, ending the code.
while choice is not 0:
    if choice == 1:
        print("\n")
        print("The sum of these numbers is ", add(num1,num2))
        print("\n")
        ans = input("Would you like to keep going? Type yes or no. ")
        if ans == 'no':
            break
        elif ans == 'yes':
            print("\n")
            printHeader()
            num1 = int(input("Enter the first number "))
            num2 = int(input("Enter the second number "))
            print("\n")
            menu()
            choice = int(input("Choose which operation the first and second number will use. "))
            
    if choice == 2:
        print("\n")
        print("The difference of these numbers is ", sub(num1,num2))
        print("\n")
        ans = input("Would you like to keep going? Type yes or no. ")
        if ans == 'no':
            break
        elif ans == 'yes':
            print("\n")
            printHeader()
            num1 = int(input("Enter the first number "))
            num2 = int(input("Enter the second number "))
            print("\n")
            menu()
            choice = int(input("Choose which operation the first and second number will use. "))
            
    if choice == 3:
        print("\n")
        print("The product of these numbers is ", mult(num1,num2))
        print("\n")
        ans = input("Would you like to keep going? Type yes or no. ")
        if ans == 'no':
            break
        elif ans == 'yes':
            print("\n")
            printHeader()
            num1 = int(input("Enter the first number "))
            num2 = int(input("Enter the second number "))
            print("\n")
            menu()
            choice = int(input("Choose which operation the first and second number will use. "))
            
    if choice == 4:
        print("\n")
        print("The quotient of these numbers is ", div(num1,num2))
        print("\n")
        ans = input("Would you like to keep going? Type yes or no. ")
        if ans == 'no':
            break
        elif ans == 'yes':
            print("\n")
            printHeader()
            num1 = int(input("Enter the first number "))
            num2 = int(input("Enter the second number "))
            print("\n")
            menu()
            choice = int(input("Choose which operation the first and second number will use. "))
            print("\n")
    


    
