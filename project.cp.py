
import turtle
turtle.showturtle()
def newSquare():
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(60)
def ask4num():
    number1, number2, number3, number4, number5, number6, number7, number8, number9 = input("Enter 9 numbers ranging only from 1-9 Example: 123456789 is 0 numbers")
    return number1, number2, number3, number4, number5, number6, number7, number8, number9
num1, num2, num3, num4, num5, num6, num7, num8, num9 = ask4num()
while(int(num1)) > 10 or (int(num1))< 1:
    print("EVERY number has to be ranging fro  1 to 9")
    num1, num2, num3, num4, num5, num6, num7, num8, num9= ask4num()
while(int(num2)) > 10 or (int(num2))< 1:
    print("EVERY number has to be ranging fro  1 to 9")
    num1, num2, num3, num4, num5, num6, num7, num8, num9= ask4num()
while(int(num3)) > 10 or (int(num3))< 1:
    print("EVERY number has to be ranging fro  1 to 9")
    num1, num2, num3, num4, num5, num6, num7, num8, num9= ask4num()
while(int(num4)) > 10 or (int(num4))< 1:
    print("EVERY number has to be ranging fro  1 to 9")
    num1, num2, num3, num4, num5, num6, num7, num8, num9= ask4num()
while(int(num5)) > 10 or (int(num5))< 1:
    print("EVERY number has to be ranging fro  1 to 9")
    num1, num2, num3, num4, num5, num6, num7, num8, num9= ask4num()
while(int(num6)) > 10 or (int(num6))< 1:
    print("EVERY number has to be ranging fro  1 to 9")
    num1, num2, num3, num4, num5, num6, num7, num8, num9= ask4num()
while(int(num7)) > 10 or (int(num7))< 1:
        print("EVERY number has to be ranging fro  1 to 9")
        num1, num2, num3, num4, num5, num6, num7, num8, num9= ask4num()
    while(int(num8)) > 10 or (int(num8))< 1:
        print("EVERY number has to be ranging fro  1 to 9")
        num1, num2, num3, num4, num5, num6, num7, num8, num9= ask4num()
    while(int(num9)) > 10 or (int(num9))< 1:
        print("EVERY number has to be ranging fro  1 to 9")
        num1, num2, num3, num4, num5, num6, num7, num8, num9= ask4num()
    turtle.speed(0)
    newSquare()
    newSquare()
    newSquare()
    turtle.right(180)
    newSquare()
    newSquare()
    newSquare()
    turtle.right(180)
    turtle.forward(180)
    turtle.right(270)
    turtle.forward(60)
    turtle.right(270)
    newSquare()
    newSquare()
    newSquare()
    turtle.penup()
    turtle.right(90)
    turtle.forward(60)
    turtle.right(45)
    turtle.right(90)
    turtle.forward(30)

main()


