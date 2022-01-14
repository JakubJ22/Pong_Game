from turtle import *


class Paddle(Turtle):

    def __init__(self, positionX):
        super().__init__()
        self.color("white")
        self.positionX = positionX
        self.penup()
        self.shape("square")
        self.setheading(90)
        self.speed("fastest")
        self.creating_paddle()
        self.y_move = 10

    def creating_paddle(self):
        self.resizemode("user")
        self.shapesize(1, 5)
        self.goto(self.positionX, 0)

    def move(self):
        """Protection against moving beyond the screen"""
        if self.ycor() > 250:
            self.goto(self.positionX, 251)

        elif self.ycor() < -250:
            self.goto(self.positionX, -251)

    def move_up(self):
        for _ in range(4):
            self.new_y = self.ycor() + self.y_move
            self.goto(self.positionX, self.new_y)

    def move_down(self):
        for _ in range(4):
            self.new_y = self.ycor() - self.y_move
            self.goto(self.positionX, self.new_y)
