from turtle import Turtle

class Brick(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.pen(fillcolor="red", pencolor='black', pensize=5)
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=3, outline=3)
        self.goto(self.x, self.y)

    def erase_brick(self):
        self.pen(fillcolor="black", pencolor='black', pensize=5)
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=3, outline=3)
        self.goto(self.x, self.y)

    def show_brick(self):
        self.pen(fillcolor="red", pencolor='black', pensize=5)
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=3, outline=3)
        self.goto(self.x, self.y)
