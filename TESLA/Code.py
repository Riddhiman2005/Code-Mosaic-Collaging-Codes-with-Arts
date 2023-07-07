import turtle

# Create an instance of the Turtle class
t = turtle.Turtle()

# Change the background color of the turtle screen
t.getscreen().bgcolor("red")

# Set the pen color to black
t.pencolor("black")

# Adjust the drawing speed of the turtle
t.speed(10)

# Set the color to white and lift the pen up
t.color("white")
t.penup()

# Reposition the turtle's starting position
t.goto(-160, 160)

# Put the pen down to start drawing
t.pendown()

# Begin the filling of the shape
t.begin_fill()

# Draw the first part of the shape
t.left(18)
t.circle(-500, 40)
t.right(90)
t.forward(17)

# Draw the second part of the shape
t.right(89.5)
t.circle(500, 39)
t.right(90)
t.forward(17)

# End the filling of the shape
t.end_fill()

# Lift the pen up and move to the next position
t.penup()
t.goto(-155, 133)
t.pendown()

# Begin the filling of the second shape
t.begin_fill()

# Draw the first part of the second shape
t.right(90.5)
t.circle(-500, 38)
t.right(70)
t.circle(-30, 80)
t.left(90)
t.circle(-20, -70)
t.right(10)
t.circle(-300, -15)
t.right(93)
t.forward(280)
t.right(160)
t.forward(280)
t.left(80)
t.circle(300, 15)
t.circle(20, 70)
t.left(80)
t.circle(30, -80)

# End the filling of the second shape
t.end_fill()

# Lift the pen up and move to the next position
t.penup()
t.goto(-20, 155)
t.pendown()

# Set the pen color to black and the shape color to red
t.pencolor("black")
t.color("red")

# Begin the filling of the third shape
t.begin_fill()

# Draw the third shape
t.left(30)
t.forward(60)
t.left(130)
t.forward(65)

# End the filling of the third shape
t.end_fill()

# Writing TESLA

# Set the pen color to white
t.pencolor("white")

# Draw the letter T
t.penup()
t.goto(-200, -180)
t.pendown()
t.right(66)
t.pensize(15)
t.forward(60)
t.back(30)
t.right(90)
t.forward(70)

# Draw the letter E
t.penup()
t.goto(-115, -180)
t.pendown()
t.left(90)
t.forward(60)
t.penup()
t.goto(-115, -215)
t.pendown()
t.forward(60)
t.penup()
t.goto(-115, -250)
t.pendown()
t.forward(60)

# Draw the letter S
t.penup()
t.goto(-20, -180)
t.pendown()
t.forward(60)
t.backward(60)
t.right(90)
t.forward(34)
t.left(90)
t.forward(60)
t.right(90)
t.forward(34)
t.right(90)
t.forward(60)

# Draw the letter L
t.penup()
t.goto(70, -180)
t.pendown()
t.left(90)
t.forward(70)
t.left(90)
t.forward(60)

# Draw the letter A
t.penup()
t.goto(155, -180)
t.pendown()
t.forward(60)
t.penup()
t.goto(155, -250)
t.pendown()
t.left(90)
t.forward(32.5)
t.right(90)
t.forward(60)
t.right(90)
t.forward(32.5)

# End the drawing
turtle.done()
