from turtle import Screen
import paddle
import ball
import time
import score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

l_paddle = paddle.Paddle((-350,0))
r_paddle = paddle.Paddle((350,0))
new_ball = ball.Ball()
l_score = score.Score((-20,280))
r_score = score.Score((20,280))

screen.listen()
screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)

screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)

game_is_on = True

while game_is_on:
    time.sleep(new_ball.ball_speed)
    screen.update()
    new_ball.ball_move()

    if new_ball.ycor() > 270 or new_ball.ycor() < -270:
        new_ball.ball_bounce_y()

    if (new_ball.distance(r_paddle) < 60 and new_ball.xcor() > 320) or (new_ball.distance(l_paddle) < 60 and new_ball.xcor() < -320):
        new_ball.ball_bounce_x()

    if new_ball.xcor() > 380 and new_ball.distance(r_paddle) > 10:
        new_ball.ball_reset()
        l_score.score += 1
        l_score.current_score()
    
    if new_ball.xcor() < -380 and new_ball.distance(l_paddle) > 10:
        new_ball.ball_reset()
        r_score.score += 1
        r_score.current_score()

    if l_score.score == 5 or r_score == 5:
        game_is_on = False
        l_score.game_end()

screen.exitonclick()