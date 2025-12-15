#Name: Kameron Burden
#Date: 8/26/2022
#Class: COMP163001.202310
#This program is meant to prompt the user to enter 2 values, those being the base and height, in order for them to be used in finding the area of a triangle


#Prompts user to enter value for base and height
base = int(input('Enter a value to be used for the base of this triangle. '))
height = int(input('Enter a value to be used for the height of this triangle. '))
#Uses values from prompts to find the area 
area = (base * height) // 2
print('The base is ', base)
print('The height is ', height)
print('By multiplying these two values, and dividing the product by 2, we can find the area of the triangle.')
#Prints out the area of the triangle
print('The area of the triangle is:', area)
