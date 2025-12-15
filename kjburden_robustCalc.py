#Name: Kameron Burden
#Date: 11/11/2022
#Class: COMP163001.202310
#Code name: kjburden_robustCalc
#This program is meant to prompt the user for 2 numbers ranging from 500 to 1000, then have the user choose which operation the numbers will use.
#This program will not crash, if an error occurs, the exception will be raised and the user will be told to try again.

#First exception
class AggieError(Exception):
    def __init__(self):
        super().__init__('Zero Value')

#Second exception
class AggieRangeError(Exception):
    def __init__(self):
        super().__init__('Invalid Range')

#This function will check if the numbers entered are in range of 500 and 1000, if not, the exception is raised and the code will end.
def answ(top, bottom):
    if bottom == 0:
        raise AggieError()
    if (top not in range(500, 1001)) or (bottom not in range(500, 1001)):
        raise AggieRangeError()
     
    
answer=''

#The 4 functions that are meant to return the value of the two numbers depending on the chosen operation    
def add(x, y):
    z = x + y
    print("The sum of these numbers is " ,z)

def sub(x, y):
    z = x - y
    print("The difference of these numbers is " ,z) 

def mult(x, y):
    z = x * y
    print("The product of these numbers is " ,z)

def div(x, y):
    z = x / y
    print("The quotient of these numbers is " ,z)

        
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
#If the number entered is not in the range of 500 and 1000, the exception will be raised.
try:
    num1 = int(input("Enter the first number, must be between 500 and 1000 "))
    num2 = int(input("Enter the second number, must be between 500 and 1000 "))
    answ(num1,num2)
    print("\n")


#If the numbers entered are within range of 500 and 1000, the menu will be displayed and you can choose your operation.
    menu()

#The prompt asks the user which operation they want to use.
    choice = int(input("Choose which operation the first and second number will use. "))




#Depending on the operation, a print statement is shown, showing thee results of the chosen operation.
#The user is the prompted to do the program again
#If the answer is yes, the menus will reappear and prompt the user for another set of numbers and another choice of operation.
#If the answer is no, the loop is broken, ending the code.


    while choice != 0:
        if choice == 1:
            print("\n")
            add(num1,num2)
            print("\n")
            ans = input("Would you like to keep going? Type yes or no. ")
            if ans == 'no':
                break
            elif ans == 'yes':
                print("\n")
                printHeader()
                num1 = int(input("Enter the first number, must be between 500 and 1000  "))
                num2 = int(input("Enter the second number, must be between 500 and 1000  "))
                answ(num1,num2)
                print("\n")
                menu()
                choice = int(input("Choose which operation the first and second number will use. "))
            
        if choice == 2:
            print("\n")
            sub(num1,num2)
            print("\n")
            ans = input("Would you like to keep going? Type yes or no. ")
            if ans == 'no':
                break
            elif ans == 'yes':
                print("\n")
                printHeader()
                num1 = int(input("Enter the first number, must be between 500 and 1000  "))
                num2 = int(input("Enter the second number, must be between 500 and 1000  "))
                answ(num1,num2)
                print("\n")
                menu()
                choice = int(input("Choose which operation the first and second number will use. "))
            
        if choice == 3:
            print("\n")
            multi(num1,num2)
            print("\n")
            ans = input("Would you like to keep going? Type yes or no. ")
            if ans == 'no':
                break
            elif ans == 'yes':
                print("\n")
                printHeader()
                num1 = int(input("Enter the first number, must be between 500 and 1000  "))
                num2 = int(input("Enter the second number, must be between 500 and 1000  "))
                answ(num1,num2)
                print("\n")
                menu()
                choice = int(input("Choose which operation the first and second number will use. "))
                
        if choice == 4:
            print("\n")
            if num2 == 0:
                raise Exception
            div(num1,num2)
            print("\n")
            ans = input("Would you like to keep going? Type yes or no. ")
            if ans == 'no':
                break
            elif ans == 'yes':
                print("\n")
                printHeader()
                num1 = int(input("Enter the first number, must be between 500 and 1000  "))
                num2 = int(input("Enter the second number, must be between 500 and 1000  "))
                answ(num1,num2)
                print("\n")
                menu()
                choice = int(input("Choose which operation the first and second number will use. "))
                print("\n")


#Custom exceptions and general exceptions made to prevent the code from crashing
    
except AggieError: 
    answer = 'Number is a 0, try again with the numbers in range.'
    print(answer)
except AggieRangeError: 
    answer = 'Value is not in range, try again with the numbers in range.'
    print(answer)
except Exception:
    answer = 'No Value, enter numbers within the range of 500 and 1000'
    print(answer)




    
