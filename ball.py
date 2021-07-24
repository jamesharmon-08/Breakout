from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.color("white")
        self.x_speed = 1
        self.y_speed = -1
        self.move_speed = 0.1
        self.reset()


    def update(self):
        x = self.xcor() + self.x_speed
        y = self.ycor() + self.y_speed
        if y > 230:
            self.bounce_y()
        if x < -190 or x > 190:
            self.bounce_x()
        self.goto(x, y)

    def reset(self):
        self.bounce_y()
        self.move_speed = 0.1
        self.goto(0,-200)

    def bounce_y(self):
        self.y_speed *= -1

    def bounce_x(self):
        self.x_speed *= -1
        self.move_speed *= 0.9

