#Name: Kameron Burden
#Date: 9/25/2022
#Class: COMP163001.202310
#This program is meant to print a random list of a random amount, and then put all the numbers in said list in order from smallest to largest.


import random
import time

#Creating an empty list with it's size randomly ranging from 10 - 20  and filling it with random numbers ranging from -50 to 50

rando = []
li = random.randint(10,21)
for n in range(li):
    rando.append(random.randint(-50,51))
    
#Printing out the random amount of random numbers
print(rando)
time.sleep(3)

#Sorting the random numbers from least to greatest
bol = True
while bol == True:
    bol = False
    point = 1
    while point < len(rando):
        if rando[point - 1] > rando[point]:
            temp = rando[point]
            bol = True
            rando[point] = rando[point- 1]
            rando[point - 1] = temp
            point +=1
        else:
            point += 1

#Printing out the random list with ordered values
print(rando)

