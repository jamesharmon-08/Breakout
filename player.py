from turtle import Turtle

PLAYER_POSITION = (0, -250)



class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.outline_color = 'black'
        self.pen(fillcolor="grey", pencolor=self.outline_color, pensize=5)
        self.penup()
        self.position = PLAYER_POSITION
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=4, outline=3)
        self.goto(self.position)
        self.lives = 3


    def paddle_left(self):
        if self.xcor() > -205+50:
            x = self.xcor() - 10
            y = self.ycor()
            self.goto(x, y)

    def paddle_right(self):
        if self.xcor() < 205-63:
            x = self.xcor() + 10
            y = self.ycor()
            self.goto(x, y)

    def reset(self):
        self.goto(self.position)