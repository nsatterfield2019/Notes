import turtle

my_turtle = turtle.Turtle()
my_turtle.showturtle()
my_turtle.shape("turtle")
my_turtle.speed(2)

my_screen = turtle.Screen()
my_screen.bgcolor('White')

# draw a shape using goto
my_turtle.fillcolor('red')
my_turtle.begin_fill() # starts a shape to fill in
my_turtle.goto(200, 0)
my_turtle.goto(200, 200)
my_turtle.goto(0, 200)
my_turtle.goto(0, 0)
my_turtle.end_fill() # end of shape

# pick up the turtle

my_turtle.up()
my_turtle.goto(200, 200)

my_turtle.fillcolor('blue')
my_turtle.begin_fill() # starts a shape to fill in
my_turtle.down()
my_turtle.goto(300, 300)
my_turtle.goto(300, 200)
my_turtle.goto(200,200)
my_turtle.end_fill()


# draw using headings
my_turtle.up()
my_turtle.goto(0, 0)
my_turtle.down()
my_turtle.width(1) # width in pixels

my_turtle.fillcolor('yellow')
my_turtle.begin_fill()
my_turtle.forward(100)
my_turtle.setheading(90)
my_turtle.forward(100)
my_turtle.setheading(180)
my_turtle.forward(100)
my_turtle.setheading(270)
my_turtle.forward(100)
my_turtle.end_fill()

for i in range(6):
    #my_turtle.right(1)
    #my_turtle.forward(1)
    my_turtle.right(60)
    my_turtle.forward(100)


# Rectangle recursive pattern
my_screen.clear()

my_turtle.home()

def recursive_rect(width, height, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(width / 2, height / 2)
        my_turtle.down()
        my_turtle.goto(width / 2, -height / 2)
        my_turtle.goto(-width / 2, -height / 2)
        my_turtle.goto(-width / 2 , height / 2)
        my_turtle.goto(width / 2, height / 2)
        recursive_rect(width * 1.5, height * 1.5, depth -1)

recursive_rect(5, 5, 8)


my_screen.clear()
# Recursive Fractal (NCAA)

def recursive_ncaa(x, y, size, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x + size, y)
        my_turtle.goto(x + size, y + size / 3)
        my_turtle.goto(x + size, y - size / 3)
        recursive_ncaa(x + size, y + size / 3, size / 3, depth - 1)
        recursive_ncaa(x + size, y - size / 3, size / 3, depth - 1)

recursive_ncaa(-300, 0, 350, 6)




my_screen.exitonclick() # end of program