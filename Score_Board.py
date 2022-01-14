from turtle import *
FONT = ('Arial', 15, 'normal')


class Score_Board(Turtle):

    def __init__(self, name, position):
        super().__init__()
        self.name = name
        self.position = position
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(position, 276)
        self.give_score()

    def give_score(self):
        """Refreshing the score """
        self.clear()
        self.write(f"{self.name}'s Score: {self.score}", align="center",
                   font=FONT)

    def game_over(self):
        self.goto(10, 10)
        self.color("white")
        self.write(f"{self.name} WON!!", align="center",
                   font=('Arial', 20, 'normal'))
