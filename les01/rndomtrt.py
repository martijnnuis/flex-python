import turtle
import random
import time

amount=(15)

turtle.color('black')
turtle.speed(amount)
for a in range(500):
    turtle.forward(600)
    turtle.left(149)
turtle.penup()
turtle.home()
turtle.pendown()
turtle.color('lightblue')
time.sleep(.2)

for b in range(125):
    turtle.forward(600)
    turtle.left(150.5)

turtle.done()