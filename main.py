from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")                # Set background color
screen.title("Snake Game")             # Set title

screen.tracer(0)                       # Turn off animation

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()                        # Listen for key press

screen.onkey(fun=snake.up, key="Up")    # Move up
screen.onkey(fun=snake.down, key="Down")    # Move down
screen.onkey(fun=snake.left, key="Left")    # Move left
screen.onkey(fun=snake.right, key="Right")    # Move right

game_is_on = True

while game_is_on:
    screen.update()                  # Update the screen
    time.sleep(0.1)                  # Add delay
    
    snake.move()                     # Move the snake

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.turtle_segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()         # Close window on click