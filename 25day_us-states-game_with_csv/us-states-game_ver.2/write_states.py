from turtle import Turtle


class State(Turtle):

    def __init__(self, state, x, y):
        super().__init__()
        self.ht()
        self.penup()
        self.goto(x, y)
        self.write(arg=state)
