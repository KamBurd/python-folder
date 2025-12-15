import turtle

turtle.showturtle()

turtle.fillcolor('red') #Used to change the color of the shape thats about to be created
turtle.begin_fill()
for i in range(8): #Loops the same command 8 times to make 8 sides for an octogon
    turtle.forward(70)
    turtle.right(45)
turtle.end_fill()
turtle.penup()
turtle.right(30)
turtle.forward(50)
turtle.right(65)
turtle.forward(80)
turtle.write('STOP', font=("ariel", 35, "normal"), align=("center")) #Used to put text into the center of the octogon to make a stop sign
turtle.hideturtle()

    

