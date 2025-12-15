#Prompts user to enter a purchase
purchase = int(input('Enter amount of purchase: '))
#Variable for sales tax, which is the given tax times the amount purchased
sales_tax = 0.05 * purchase
#Variable for country tax, which is the given tax times the amount purchased
country_tax = 0.025 * purchase
#Variable for total ttax, which is the sales and country tax added together
total_tax = sales_tax + country_tax
#The total amount of money
total = purchase + total_tax
print('Purchase Amount:', purchase)
print('State Tax:', sales_tax)
print('County Tax:', country_tax)
print('Total Tax:', total_tax)
print('Sale Total:', total)
