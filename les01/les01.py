from asyncore import loop
from random import randint, random
import turtle


turtle.color('black')
turtle.begin_fill()

for a in range(8):
    turtle.forward(100)
    turtle.left(45)

turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(50)

turtle.left(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(30)

turtle.penup()
turtle.left(180)
turtle.forward(30)
turtle.right(90)
turtle.forward(25)
turtle.pendown()
turtle.circle(75)
turtle.penup()
turtle.left(90)
turtle.forward(20)
turtle.pendown()
turtle.fillcolor("yellow")

turtle.done()