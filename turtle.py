import turtle

turtle = turtle.Turtle()

# Square

def square(length):  # The parameter 'length' is passed
  turtle.forward(length)
  turtle.left(90)
  turtle.forward(length)
  turtle.left(90)
  turtle.forward(length)
  turtle.left(90)
  turtle.forward(length)
  turtle.left(90)

# This is saying everytime you see 'length' make it to 150
square(150)

# This is saying everytime you see 'length' make it to 300
square(300)

# This is saying everytime you see 'length' make it to 600
square(600)

# This is saying everytime you see 'length' make it to 150/2
square(150/2)

