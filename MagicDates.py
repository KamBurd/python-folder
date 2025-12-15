# Asks user for month
month = int(input("What is the month? Enter in number form in 2 digits."))
#Asks user for day
day = int(input('What is the day? Enter 2 digits'))
#Asks user for year
year = int(input('What is the year? Enter 2 digits'))
#If the month times the day is the year, it prints a messages, otherwise, it prints another message
if(month * day == year):
    print('The date is', month, '/', day, '/', year)
    print('Wow! This date is magic!')
else:
        print('The date is', month,'/',day, '/',year)
        print('This date is not magic')
    

