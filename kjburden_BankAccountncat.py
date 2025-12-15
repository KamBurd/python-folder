#  NCAT Kameron Burden
#  COMP-163 : Section 01
#  Instructor : Derrick Leflore
#  Description : Making BankAccount Class from UML document
# naming convention : kjburden_BankAccountncat.py


class BankAccount:
    # ** Var declarations Typing
    balance:int
    customerId:int
    customerName:str
    prevTransaction= ['0']  
    
    # ** Class Var declarations

    # Constructor
    def __init__(self, customerName, customerId):
        # ** Instance Var declarations
        
        self.balance = 0
        self.prevTransaction=['0']
        self.withdraw = 0
        self.deposit = 0
        print('Welcome to Aggie Bank Account')
        print('*****************************')
        self.customerName = input('What\'s your name? ')
        self.customerID = input('Enter your ID number (just make it random 5 numbers) ')
        print('\n')

        
	# ** Get/Set functionszz
    def getBalance(self):
        return self.balance
    
    def setBalance(self, getBalance):
        self.balance = getBalance
        
    def getCustomerId(self):
        return self.customerId
    
    def setCustomerID(self, getcustomerId):
        self.customerId = getcustomerId
        
    def getCustomerName(self):
        return self.customerName
    
    def setCustomerName(self,getCustomerName):
        self.customerName = getCustomerName

  #If the value 0 in the prevTransaction list is present, then no transaction occured, but if a transaction occured before choosing the 'd' option, that previous transaction will be printed.
    def getPreviousTransaction(self):
        if '0' in self.prevTransaction:
            print('No transaction occured')
        else:
            print(self.prevTransaction[0])
      
      
            
        
            
    
    def setPreviousTransaction(self,getPrevTrans):
        self.prevTransaction = getPrevTransaction

#Withdraw and Deposit Functions
#Will pop the '0' thats currently in the list and append the previous transaction.
    def withdra(self):
        amount = int(input('Enter amount to withdraw: '))
     
        self.balance = self.balance - amount
        self.prevTransaction.pop(0)
        self.prevTransaction.append(f'Withdrawn: ${amount}')
        
        
        
        return amount
        
    def deposi(self):
        amount = int(input('Enter amount to deposit: '))
       
        self.balance = self.balance + amount
        self.prevTransaction.pop(0)
        self.prevTransaction.append(f'Deposited: ${amount}')
      
        return amount


    

 

    def __str__(self):
        return BankAccount

