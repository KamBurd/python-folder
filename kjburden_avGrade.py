#Name: Kameron Burden
#Date: 9/4/2022
#Class: COMP163001.202310
#This program is meant to prompt the user to enter 5 student quiz grades. The 5 grades are then added in a list, and then averaged, printing out the average score.

#Prompts the user to enter the 5 quiz grades for the students.
grades = 0
grade1 = float(input('Enter the quiz grade of the first student '))
grade2 = float(input('Enter the quiz grade of the sceond student '))
grade3 = float(input('Enter the quiz grade of the third student '))
grade4 = float(input('Enter the quiz grade of the fourth student '))
grade5 = float(input('Enter the quiz grade of the fifth student '))
#Assembles the grades that the user entered into a list
grades = [grade1, grade2, grade3, grade4, grade5]
#Adds the values in the list together, then divides the value by the number of values in the list. (This list has 5 values)
average = sum(grades) / len(grades)
#Prints the grades entered, and then prints the average.
print(f'The grades entered were: {(grades)}.')
print(f'The average of all {len(grades)} grades is: {average}')











