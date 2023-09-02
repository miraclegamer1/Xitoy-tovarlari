import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle instance
pen = turtle.Turtle()
pen.speed(2)  # Set the drawing speed

# Set the color and fill color for the logo
pen.color("#E1306C")
pen.fillcolor("#E1306C")

# Draw the camera shape
pen.begin_fill()
pen.circle(50)
pen.end_fill()

# Draw the lens
pen.up()
pen.goto(-15, 0)
pen.down()
pen.setheading(180)
pen.width(10)
pen.circle(15)

# Hide the turtle
pen.hideturtle()

# Exit on click
turtle.done()