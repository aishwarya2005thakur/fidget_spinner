from turtle import *

# State to keep track of the spinner's turn
state = {'turn': 0}

def spinner():
    clear()
    angle = state['turn'] / 10
    right(angle)

    # Draw the red dot
    forward(100)
    dot(120, 'red')
    back(100)

    # Draw the green dot
    right(120)
    forward(100)
    dot(120, 'green')
    back(100)

    # Draw the blue dot
    right(120)
    forward(100)
    dot(120, 'blue')
    back(100)

    # Update the display
    update()

def animate():
    if state['turn'] > 0:
        state['turn'] -= 0.1

    spinner()
    ontimer(animate, 150)

def flick():
    state['turn'] += 10

# Setup the turtle environment
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
width(20)

# Bind the flick function to the space key
onkey(flick, 'space')
listen()

# Start the animation
animate()
done()
