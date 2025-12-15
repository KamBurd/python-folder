#  NCAT Kameron Burden
#  COMP-163 : Section 01
#  Instructor : Derrick Leflore
#  Description : Making BankAccount Class from UML document
# naming convention : kjburden_BankingApplication.py



#Make this more persistant (even if code is closed, the data still remains)

#Imports file
import kjburden_BankAccountncat
#Creates object from seperate file to use in this file
bank = kjburden_BankAccountncat.BankAccount(0,0)
account = []

#Option menu
def showMenu():
    print('*****************************')
    print('A. Check Balance')
    print('B. Deposit')
    print('C. Withdraw')
    print('D. Previous Balance')
    print('E. Exit')

#Option prompt function
def getMenuOpt():
    print('======================================')
    opt=input('Enter an option: ').upper()
    print('======================================')
    print(opt)
    return opt
    
     
#Welcome message
print('******************')
print('Aggie Bank Account')
print(f'Customer Name: {bank.customerName}')
print(f'Customer ID: {bank.customerID}')
print('\n')
print('*****************************')
print(f'Welcome {bank.customerName}.')
print(f'Your ID is {bank.customerID}')
print('\n')
showMenu()

#Prints a message regarding your bank account on the option chosen.
option = getMenuOpt()
while option != 'E':
    if option == 'A':
        print('Current Balance: $',bank.getBalance())
    if option == 'B':
        amount = bank.deposi()
        print(f'${amount} was deposited')
    if option == 'C':
        witha = bank.withdra()
        print(f'${witha} was withdrawn')
    if option =='D':
        bank.getPreviousTransaction()
    option = getMenuOpt()

print(f'Thank you {bank.customerName} for using Aggie Bank!')


 
