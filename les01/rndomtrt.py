import turtle
import random
import time

amount=(200)

turtle.color('blue')
turtle.speed(amount)
time.sleep(2)
for a in range(976):
    turtle.forward(600)
    turtle.left(149.5)

turtle.penup()
turtle.home()
turtle.pendown()
turtle.color('red')
time.sleep(.2)

for b in range(244):
    turtle.forward(600)
    turtle.left(150.5)

turtle.penup()
turtle.home()
turtle.pendown()
turtle.color('green')

for c in range(122):
    turtle.forward(600)
    turtle.left(150.25)

turtle.done()