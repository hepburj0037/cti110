# Write your initials using turtle.
# 09/24/2018
# CTI-110 P4T1b - Initials
# Joshua Hepburn
#

# Allow us to use turtles.
import turtle

# Create a playground.
wn = turtle.Screen()

# Color of background.
wn.bgcolor("lightblue")

# Create a turtle and assigned to a name.
alex = turtle.Turtle()

# Color of Alex.
alex.color("red")

# Pen size.
alex.pensize(4)

# Increased speed.
alex.speed(10)

# The initial J H.
alex.left(90)
alex.forward(100)
alex.left(90)
alex.forward(50)
alex.left(180)
alex.forward(100)
alex.left(180)
alex.forward(50)
alex.left(90)
alex.forward(100)
alex.left(270)
alex.forward(50)
alex.left(270)
alex.forward(50)
alex.left(180)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.penup()
alex.forward(100)
alex.pendown()
alex.left(90)
alex.forward(100)
alex.left(180)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(180)
alex.forward(100)

wn.mainloop()
