from turtle import *
from Paddle import Paddle
from Score_Board import Score_Board
from ball import Ball
import time

screen = Screen()

"""Setting up the screen settings"""
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)
screen.title("Pong")

"""Creating a tool to draw our middle line"""
middle_line = Turtle(visible=False)
middle_line.penup()
middle_line.goto(0, -287)
middle_line.setheading(90)
middle_line.pencolor("white")
middle_line.pendown()
middle_line.speed("fastest")

"""Drawing a line through the middle"""
for _ in range(22):
    middle_line.forward(15)
    middle_line.penup()
    middle_line.forward(15)
    middle_line.pendown()

"""Names below will be used in our score board"""
names = screen.textinput("Hello into ping game.",
                         "Enter your names separated by space.")
names = names.split()

while len(names) != 2:
    names = screen.textinput("Hello into ping game.",
                             "Two and only two players are allowed. Enter your names separated by space.")
    names = names.split()

name1 = names[0].capitalize()
name2 = names[1].capitalize()

"""Crating all needed objects"""
paddle1 = Paddle(370)
paddle2 = Paddle(-370)
board1 = Score_Board(name1, -230)
board2 = Score_Board(name2, 230)
ball = Ball()

"""Steering paddles"""
screen.onkeypress(paddle1.move_down, "Down")
screen.onkeypress(paddle1.move_up, "Up")
screen.onkeypress(paddle2.move_down, "s")
screen.onkeypress(paddle2.move_up, "w")
screen.listen()

delay = 0.04
is_game_on = True
while is_game_on:

    """time.sleep slows down our game"""
    time.sleep(delay)

    paddle1.move()
    paddle2.move()
    ball.move_ball()

    """Ball gets out of the screen (right side) and increase the score"""
    if ball.xcor() > 500:

        delay = 0.04
        ball.start_position()
        paddle1.goto(370, 0)
        paddle2.goto(-370, 0)
        board1.score += 1
        board1.give_score()

        """Ball gets out of the screen (left side) and increase the score"""
    elif ball.xcor() < - 500:
        delay = 0.04
        paddle1.goto(370, 0)
        paddle2.goto(-370, 0)
        ball.start_position()
        board2.score += 1
        board2.give_score()

    """Ball logic after it hits a paddle"""
    if (ball.distance(paddle1) < 60 and ball.xcor() == 360) or (ball.distance(paddle2) < 60 and ball.xcor() == -360):
        ball.paddle_bounce()
        if delay > 0.004:
            delay -= 0.003

    """Ball logic after it hits ceiling or floor"""
    if ball.ycor() > 280 or ball.ycor() < -280:

        ball.wall_bounce()

    """Showing up the winner"""

    if board1.score == 10:
        board1.game_over()
        is_game_on = False

    elif board2.score == 10:
        board2.game_over()
        is_game_on = False

    """refreshing screen"""
    screen.update()


screen.exitonclick()
