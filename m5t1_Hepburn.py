# Making a square and triangle using turtle.
# 09/24/2018
# CTI-110 P4T1a - Shapes
# Joshua Hepburn
#

# Allow us to use turtles.
import turtle

# Create a playground.
wn = turtle.Screen()

# Create a turtle and assigned to a name.
alex = turtle.Turtle()

# Create a square and tell the turtle where to go.
for i in range(4):
    alex.forward(50)
    alex.left(90)

# Create a square and tell the turtle where to go.
for i in range(3):
    alex.forward(80)
    alex.left(120)

# Close window.
wn.mainloop()
