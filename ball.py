from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def ball_move(self):
        self.goto(x=self.xcor()+self.x_move, y=self.ycor()+self.y_move)

    def ball_bounce_y(self):
        self.y_move *= -1

    def ball_bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def ball_reset(self):
        self.goto(0,0)
        self.ball_speed = 0.1
        self.ball_bounce_x()