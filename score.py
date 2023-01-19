from turtle import Turtle

FONT=('courier', 20, 'normal')
ALIGNMENT = 'center'

class Score(Turtle):
    
    def __init__(self, pos):
        super().__init__()
        self.score=0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(pos)
        self.current_score()

    def current_score(self):
        self.clear()
        self.write(arg=f"{self.score}", align=ALIGNMENT, font=FONT)

    def game_end(self):
        self.goto(0,0)
        self.write(arg="Game Over!", align=ALIGNMENT, font=FONT)