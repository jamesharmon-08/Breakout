from turtle import Turtle


class ScreenLayout(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setheading(0)
        self.goto(-205, 250)
        self.pendown()
        self.forward(410)
        self.penup()

