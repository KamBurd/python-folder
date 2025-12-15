#Name: Kameron Burden
#Date: 9/9/2022
#Class: COMP163001.202310
#This program is meant to print the smallest number of frustration with the next smallest, next largest, and middle numbers

import math
import random


#Makes an empty list, and prompts the user for the size of the list.

line = []
n = int(input("Enter the size of the line, make sure the size is at least 5 "))
if n == 2 or n == 3 or n == 4 or n == 1:
    print("Invalid")
else:
#Adds random values depending on the size of the list that you enetered.
    for i in range(n):
        line.append(random.randint( -1000000000, 1000000000))
#Sorts the random values into numbered order.
    line.sort()
    print(line)
#Uses the values of the next smallest number, the value of the middle number, and the larger number after.
    area = (line[1] + line[2]) / 2
    frust = (line[2] + line[3]) / 2
#Finds the value of the smallest area of frustration.
    of = (area - frust)
#Turns the area positive in case of negative numbers.
    stration = math.fabs(of)
#Prints the value of the smallest area of frustration.
    print(f'{stration:.1f}')




