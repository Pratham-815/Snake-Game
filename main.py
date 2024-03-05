from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")                # Set background color
screen.title("Snake Game")             # Set title

screen.tracer(0)                       # Turn off animation

snake = Snake()

game_is_on = True

while game_is_on:
    screen.update()                  # Update the screen
    time.sleep(0.1)                  # Add delay
    
    snake.move()                     # Move the snake



screen.exitonclick()         # Close window on click
