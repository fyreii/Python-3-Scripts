import turtle
import math

"""

Teresa Henderson
CST 100 - Bansal
05/23/2016

assign2.py

Draws Frosty the Snowman with turtles

5/26/2016 - added the use of turtle.tracer and turtle.update to
speed up render time of picture.  Used to take upwards of 45 seconds,
now takes 2 milliseconds. Also fixed typo in last line of comments.

"""

# Create the window to run in
window = turtle.Screen()
# Make the background color of the window blue
window.bgcolor("blue")

# Instantiate "Bob" the Turtle
# He draws shapes
bob = turtle.Turtle()
# Instantiate "Martha" the Turtle
# She draws fine details
martha = turtle.Turtle()
# Instantiate "Joe" the Turtle
joe = turtle.Turtle()
# Instantiate "Tess" the Turtle
# She draws the trees
tess = turtle.Turtle()

turtle.tracer(0, 0)

# Set attributes of Bob
bob.speed(0)
bob.color("black")
bob.pensize(2)
# Set attributes of Martha
martha.speed(0)
martha.color("black")
martha.pensize(2)
# Set attributes of Joe
joe.speed(0)
joe.color("black")
joe.pensize(2)
# Set attributes of Tess
tess.speed(0)
tess.color("brown")
tess.pensize(2)


# Define the "draw polygon" function to draw a
# polygon as close to 360 degrees as we can get

def drawPolygon (t, sideLength, numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        t.forward(sideLength)
        t.right(turnAngle)


# Define the "draw filled circle" function to
# utilize the already drawn polygon from above
# to draw a circle with the named turtle and
# radius.  Then fill it in with the color
# passed as a parameter.

def drawFilledCircle (anyTurtle, color, radius):
    anyTurtle.hideturtle()
    anyTurtle.pen(fillcolor=color, pensize=3)
    anyTurtle.begin_fill()
    circumference = 2 * math.pi * radius
    sideLength = circumference / 360
    drawPolygon(anyTurtle, sideLength, 360)
    anyTurtle.end_fill()


# Define the "draw filled rectangle" function to
# draw a filled rectangle of the given dimensions and color

def drawFilledRectangle (anyTurtle, color, length, width):
    anyTurtle.hideturtle()
    anyTurtle.pen(fillcolor=color, pensize=3)
    anyTurtle.begin_fill()
    for i in range(4):
        anyTurtle.forward(length)
        anyTurtle.left(90)
        anyTurtle.forward(width)
        anyTurtle.left(90)
    anyTurtle.end_fill()


# Define the "draw filled triangle" function to draw
# a filled triangle of the given dimensions and color

def drawFilledTriangle (anyTurtle, color, base, height):
    anyTurtle.hideturtle()
    anyTurtle.pen(fillcolor=color, pensize=2)
    anyTurtle.begin_fill()
    for i in range(3):
        anyTurtle.forward(base)
        anyTurtle.right(120)
        anyTurtle.forward(height)
    anyTurtle.end_fill()


# Move Bob to the first starting position for the Body
bob.penup()
bob.goto(0, -95)
bob.pendown()
drawFilledCircle(bob, "white", 150)

# Move Bob to the second starting position for the Body
bob.penup()
bob.goto(0, 103)
bob.pendown()
drawFilledCircle(bob, "white", 100)

# Move Bob to the third starting position for the Head
bob.penup()
bob.goto(0, 250)
bob.pendown()
drawFilledCircle(bob, "white", 75)

# Move Bob to first starting position for the Hat
bob.penup()
bob.color("gray")
bob.goto(-35, 275)
bob.pendown()
drawFilledRectangle(bob, "black", 70, 100)

# Move Bob to the second starting position for the Hat
bob.penup()
bob.goto(-70, 250)
bob.pendown()
drawFilledRectangle(bob, "black", 140, 30)

# Move Bob to the first starting position for the Nose
bob.penup()
bob.color("orange")
bob.goto(12, 180)
bob.pendown()
drawFilledTriangle(bob, "orange", 5, 30)

# Move Bob to the starting position for the Pipe
bob.penup()
bob.goto(30, 135)
bob.color("brown")
bob.pendown()
drawFilledRectangle(bob, "brown", 65, 5)
bob.goto(95, 135)
drawFilledRectangle(bob, "brown", 30, 30)

# Move Bob to the first starting position for the Flower
bob.penup()
bob.color("red")
bob.goto(60, 320)
bob.pendown()
for i in range(5):
    drawFilledTriangle(bob, "red", 5, 10)
    bob.forward(5)
    bob.left(90)
bob.color("green")
bob.left(145)
bob.forward(40)

# Joe takes over and draws the arms

# Move Joe to the starting position for Arm #1
# Draw the first arm
joe.penup()
joe.pensize(10)
joe.goto(-102, 0)
joe.color("brown")
joe.right(180)
joe.pendown()
joe.forward(100)
joe.right(45)
joe.forward(70)

# Draw the first hand
joe.right(45)
joe.forward(30)
joe.penup()
joe.goto(-257, 50)
joe.left(45)
joe.pendown()
joe.forward(30)

# Move Joe to the starting position for Arm #2
# Draw the second arm
joe.penup()
joe.left(225)
joe.goto(103, 0)
joe.pendown()
joe.forward(100)
joe.left(45)
joe.forward(70)

# Draw the second hand
joe.left(45)
joe.forward(30)
joe.penup()
joe.goto(250, 50)
joe.left(45)
joe.pendown()
joe.forward(30)

# Martha takes over and draws the details

# Make Martha a circle to stamp the fine details
martha.shape("circle")

# Move Martha to the first position for the Eyes
# Draw the eyes with stamp
martha.penup()
martha.color("blue")
martha.goto(-30, 200)
martha.stamp()
martha.goto(30, 200)
martha.stamp()

# Move Martha to the first position for the mouth
# Draw the mouth with stamp

martha.penup()
martha.color("black")
martha.right(130)
martha.goto(25, 135)
size = 10
for i in range(6):
    martha.stamp()
    size = size + 1
    martha.forward(size)
    martha.right(24)

# Move Martha to the first position for buttons
# Draw the buttons with stamp
martha.penup()
martha.color("purple")
martha.goto(0, 80)
martha.stamp()
martha.goto(0, 40)
martha.stamp()
martha.goto(0, 0)
martha.stamp()
martha.goto(0, -40)
martha.stamp()
martha.goto(0, -80)
martha.stamp()

# Move Tess to the first position for trees

tess.penup()
tess.goto(-400, -400)
drawFilledRectangle(tess, "brown", 30, 300)
tess.color("green")
tess.goto(-400, -100)
tess.right(180)
drawFilledTriangle(tess, "green", 80, 100)
tess.penup()
tess.goto(-400, -200)
tess.pendown()
drawFilledTriangle(tess, "green", 80, 100)
tess.penup()
tess.goto(-400, -300)
tess.pendown()
drawFilledTriangle(tess, "green", 80, 100)

# Move Tess to the second position for trees

tess.penup()
tess.goto(415, -100)
drawFilledRectangle(tess, "brown", 30, 300)
tess.color("green")
tess.goto(400, -100)
drawFilledTriangle(tess, "green", 80, 100)
tess.penup()
tess.goto(400, -200)
tess.pendown()
drawFilledTriangle(tess, "green", 80, 100)
tess.penup()
tess.goto(400, -300)
tess.pendown()
drawFilledTriangle(tess, "green", 80, 100)

turtle.update()
# Set the "exit on click" switch so that our
# window closes on receiving a mouse click
turtle.exitonclick()


