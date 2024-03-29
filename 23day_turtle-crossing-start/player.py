from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)

    def reset(self):
        self.goto(STARTING_POSITION)



