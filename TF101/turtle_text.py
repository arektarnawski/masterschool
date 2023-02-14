def initialize_turtle(pensize = 2, speed = 5):
    """Import the library and create Turtle and Screen objects. Move the turtle to the beginning of the screen. Choice of pensize and speed."""

    import turtle as tt

    screen = tt.Screen()

    turtle = tt.Turtle()

    turtle.pensize(pensize)
    turtle.speed(speed)

    turtle.penup()
    turtle.goto(-250,0)
    turtle.pendown()

    return turtle, screen

def clear_state(turtle, final_pos):
    """ After drawing a letter, move the turtle to where a new letter can be drawn from """

    turtle.penup()
    turtle.goto(final_pos[0]+20,0)

    turtle.setheading(0)
    turtle.pendown()

def abort_turtle(turtle,screen):
    """ Hide turtle if everything has already been drawn and enable closing the screen with a click """
    turtle.hideturtle()
    screen.exitonclick()

def letter_a(turtle, color = 'black'):
    """ Writes a letter 'a' with a chosen color """
    turtle.pencolor(color)

    starting_position = turtle.pos()

    turtle.left(80)
    turtle.forward(100)

    upper_pos = turtle.pos()

    turtle.right(160)
    turtle.forward(100)

    lower_pos_right = turtle.pos()

    middle_pos_right = ( (upper_pos[0]+lower_pos_right[0])/2, (upper_pos[1]+lower_pos_right[1])/2 )
    middle_pos_left = ( (upper_pos[0]+starting_position[0])/2, (upper_pos[1]+starting_position[1])/2 )

    turtle.penup()
    turtle.goto(middle_pos_right)

    turtle.pendown()
    turtle.goto(middle_pos_left)

    turtle.penup()
    turtle.goto(lower_pos_right)

    final_pos = turtle.pos()

    clear_state(turtle, final_pos)

def letter_r(turtle, color = "black"):
    """ Writes a letter 'r' with a chosen color """
    turtle.pencolor(color)

    turtle.left(90)
    turtle.forward(100)

    turtle.right(90)

    turtle.circle(-25,90)
    right_outermost_position = turtle.pos()
    turtle.circle(-25,90)

    turtle.left(110)
    turtle.goto(right_outermost_position[0],0)

    final_pos = turtle.pos()

    clear_state(turtle, final_pos)

def letter_e(turtle, color = "black"):
    """ Writes a letter 'e' with a chosen color """
    turtle.pencolor(color)

    starting_pos = turtle.pos()

    turtle.left(90)
    turtle.forward(100)

    turtle.right(90)
    turtle.forward(25)

    turtle.penup()
    turtle.goto(starting_pos[0], starting_pos[1]+50)

    turtle.pendown()
    turtle.forward(15)

    turtle.penup()
    turtle.goto(starting_pos[0], 0)

    turtle.pendown()
    turtle.forward(25)

    final_pos = turtle.pos()

    clear_state(turtle, final_pos)

def letter_k(turtle, color = "black"):
    """ Writes a letter 'k' with a chosen color """
    turtle.pencolor(color)

    turtle.left(90)
    turtle.forward(100)

    upward_pos = turtle.pos()

    turtle.penup()
    turtle.goto(upward_pos[0], upward_pos[1]/2)

    turtle.pendown()
    turtle.goto(upward_pos[0]+35,upward_pos[1])

    turtle.penup()
    turtle.goto(upward_pos[0], upward_pos[1]/2)

    turtle.pendown()
    turtle.goto(upward_pos[0]+35, 0)

    final_pos = turtle.pos()

    clear_state(turtle, final_pos)