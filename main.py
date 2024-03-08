from turtle import Turtle,Screen
from slider import Slider
from ball import Ball
from scoreboard import Scoreboard
import random
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer()

pen = Turtle()
pen.color("white")
pen.width(5)
pen.penup()
pen.goto(0,300)
pen.setheading(270)
pen.pendown()
pen.forward(66.67)
for i in range(4):
    pen.penup()
    pen.forward(66.67)
    pen.pendown()
    pen.forward(66.67)
pen.hideturtle()

right_slider = Slider((395,0))
left_slider = Slider((-399,0))
ball = Ball()
screen.update()
right_or_left = random.randint(0,2)
if right_or_left == 0:
    ball.random_direction_right()
else:
    ball.random_direction_left()

player_right = screen.textinput("Player names", "Right player's name: ")
player_left = screen.textinput("Player names", "Left player's name: ")
scoreboard_right = Scoreboard(player_right,(200,240))
scoreboard_left = Scoreboard(player_left,(-200,240))
score_right = 0
score_left = 0

screen.listen()
screen.onkey(key="Up",fun=right_slider.up)
screen.onkey(key="Down",fun=right_slider.down)
screen.onkey(key="w",fun=left_slider.up)
screen.onkey(key="s",fun=left_slider.down)

BALL_SPEED = 5
game_on = True
while game_on:
    #print(right_slider.pos())
    screen.update()
    time.sleep(0.001)
    if score_right != 0 and score_left != 0:
        if (score_right + score_left)%20 = 0:
            BALL_SPEED += 3
    if ball.distance(right_slider.pos()) <= 35:
        ball.random_direction_left()
        score_right += 1
        scoreboard_right.refresh(score_right)
    if ball.distance(left_slider.pos()) <= 35:
        ball.random_direction_right()
        score_left += 1
        scoreboard_left.refresh(score_left)
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        heading = -ball.heading()
        ball.setheading(heading)
    ball.forward(BALL_SPEED)
    if ball.xcor() >= 390 or ball.xcor() <= -390:
        game_on = False
        if ball.xcor()>=390:
            winner = player_left
        elif ball.xcor()<=-390:
            winner = player_right
        scoreboard_right.game_over(winner)


screen.exitonclick()





