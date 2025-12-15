amount = int(input("Enter the total change"))

if amount < 10 and amount > 1:
    print(f'{amount} Pennies')
elif amount == 1:
    print(f'{amount} Penny')
elif amount < 1:
    print("No change")
    
if amount > 10 and amount < 25:
    print(f'{amount // 10} dimes')
    print(f'{amount % 10} pennies')
elif amount == 10:
    print(f'{amount // 10} dime')
    
