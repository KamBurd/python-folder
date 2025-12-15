user_input = int(input())
if user_input > 0:    
    dollar = user_input // 100
    user_input %= 100
    quarter = user_input // 25
    user_input %=25
    dime = user_input //10
    user_input %= 10
    nickel = user_input // 5
    user_input %= 5
    penny = user_input
    
    if dollar == 1:
        print(dollar, "Dollar")
    elif dollar > 1: 
        print(dollar, "Dollars")
    if quarter == 1:
        print(quarter, "Quarter")
    elif quarter > 1: 
        print(quarter, "Quarters")
    if dime == 1:
        print(dime, "Dime")
    elif dime > 1: 
        print(dime, "Dimes")    
    if nickel == 1:
        print(nickel, "Nickel")
    elif nickel > 1: 
        print(nickel, "Nickels")    
    if penny == 1:
        print(penny, "Penny")
    elif penny > 1: 
        print(penny, "Pennies")
else:
    print("No change")
