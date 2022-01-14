from turtle import *
import random



class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.6)
        self.x_move = 10
        self.y_move = 10
        self.start_position()

    def move_ball(self):
        
        self.new_x = self.xcor() + self.x_move
        self.new_y = self.ycor() + self.y_move
        self.goto(self.new_x, self.new_y)

    def start_position(self):
        """reset ball position"""
        self.goto(0, 0)
        self.y_move *= -1
        self.x_move *= -1

    def wall_bounce(self):
        self.y_move = -self.y_move

    def paddle_bounce(self):
        self.x_move = -self.x_move
