from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")                # Set background color
screen.title("Snake Game")             # Set title

screen.tracer(0)                       # Turn off animation

# Create 3 snake segments
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

turtle_segments = []

for position in starting_positions:
    tom = Turtle(shape="square")
    tom.color("white")
    tom.speed('normal')
    tom.penup()
    tom.setpos(position)
    turtle_segments.append(tom)


game_is_on = True
while game_is_on:
    screen.update()                  # Update the screen
    time.sleep(0.1)                  # Add delay
    
    for seg_num in range(len(turtle_segments) - 1, 0, -1):
        new_x = turtle_segments[seg_num-1].xcor()
        new_y = turtle_segments[seg_num-1].ycor()
        turtle_segments[seg_num].goto(new_x, new_y)
        
    turtle_segments[0].forward(20)     # Move the first segment forward



screen.exitonclick()         # Close window on click
