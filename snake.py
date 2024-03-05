from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        # Create 3 snake segments for the snake body

        self.turtle_segments = []
        self.create_snake()


    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.speed('normal')
            new_segment.penup()
            new_segment.setpos(position)
            self.turtle_segments.append(new_segment)


    def move(self):
        for seg_num in range(len(self.turtle_segments) - 1, 0, -1):
            new_x = self.turtle_segments[seg_num-1].xcor()
            new_y = self.turtle_segments[seg_num-1].ycor()
            self.turtle_segments[seg_num].goto(new_x, new_y)
        
        self.turtle_segments[0].forward(20)