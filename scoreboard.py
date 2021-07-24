from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 35, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.high_score = 6
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score:{self.player_score}         High:{self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.player_score += 1
        self.clear()
        self.update_score()

    def gameover(self):
        if self.player_score > self.high_score:
            self.high_score = self.player_score
            self.clear()
            self.update_score()
        self.goto(0,0)
        self.write("Game Over", align = ALIGNMENT, font=FONT)
