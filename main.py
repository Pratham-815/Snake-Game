from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")                # Set background color
screen.title("Snake Game")             # Set title

# Create 3 snake segments
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_positions:
    tom = Turtle(shape="square")
    tom.speed(0)
    tom.color("white")
    tom.penup()
    tom.setpos(position)







screen.exitonclick()         # Close window on click
