from turtle import Screen
from screen import ScreenLayout
from player import Player
from wall import Wall
from ball import Ball
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=410, height=600)
screen.bgcolor("black")
screen.title("BreakOut")
screen.tracer(0)

layout = ScreenLayout()
wall = Wall()
player = Player()
ball = Ball()
score = ScoreBoard()

is_playing = True

while is_playing:
    screen.update()
    # wall.display_wall()
    ball.update()
    if wall.collision(ball):
        score.increase_score()
        if score.player_score % 18 == 0:
            player.reset()
            wall.reset_wall()
            ball.reset()

    if ball.distance(player) < 25:
        if ball.y_speed < 0:
            ball.bounce_y()
    if ball.ycor() < -250:
        player.lives -= 1
        if player.lives == 0:
            score.gameover()
            is_playing = False
        else:
            ball.reset()

    screen.listen()
    screen.onkeypress(player.paddle_left, 'Left')
    screen.onkeypress(player.paddle_right, 'Right')

screen.exitonclick()
