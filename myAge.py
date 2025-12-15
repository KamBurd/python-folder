#Name: Kameron Burden
#Date: 8/22/2022
#Class: COMP163001.202310
#This program is meant to 
import math
x = float(input())
y = float(input())
z = float(input())
print(f'{math.pow(x,z):.2f} ', end='')
print(f'{math.pow(x, (y**z)):.2f} ', end='')
print(f'{math.fabs(x - y):.2f} ', end='')
print(f'{math.sqrt(math.pow(x,z)):.2f}')
