from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
    
        self.shape('square')
        self.shapesize(5,1,10)
        self.penup()
        self.color('white')
        self.goto(pos)
        
    def move_up(self):
        self.goto(x=self.xcor(),y=self.ycor()+20)


    def move_down(self):
        self.goto(x=self.xcor(),y=self.ycor()-20)

    
