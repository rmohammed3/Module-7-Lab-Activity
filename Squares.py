# Raheemuddin Mohammed
# August 27, 2025

# Problem 5: Draw a square using turtle graphics

import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""
    for i in range(4):
        t.forward(sz)
        t.left(90)

# Setup screen and turtle
wn = turtle.Screen()
alex = turtle.Turtle()
alex.color("blue")

# Draw a series of squares with increasing sizes
for size in range(20, 120, 20):  # sizes: 20, 40, 60, 80, 100
    drawSquare(alex, size)
    alex.penup()
    alex.backward(10)  # shift position so spiral looks centered
    alex.right(90)
    alex.forward(10)
    alex.left(90)
    alex.pendown()

wn.exitonclick()
