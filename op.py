def addMe(val1,val2):
    mySum = val1 + val2
    return mySum
def printHeader():
    print("Welcome to Aggie Application")
    print("============================")
    print('\n')

printHeader()    
op1 = int(input('Enter op1 '))
op2 = int(input('Enter op2 '))
answer = addMe(op1,op2)
print(f'The sum is {str(answer)}.')
