from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from bricks import Bricks
import time

game_is_on = True

# Display a Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("BreakOut Game")
screen.tracer(0)

# Display the Paddles
paddle = Paddle((0, -250))

# Display the ball
ball = Ball()

# Display Bricks
bricks = Bricks()

# Display Scoreboard
scoreboard = Scoreboard()

screen.listen()

screen.onkey(key="a", fun=paddle.go_left)
screen.onkey(key="d", fun=paddle.go_right)
screen.onkey(key="Left", fun=paddle.go_left)
screen.onkey(key="Right", fun=paddle.go_right)

# create bricks
bricks.create_bricks()

sleep_timer = 0.1
while game_is_on:
    screen.update()
    if sleep_timer < 0:
        sleep_timer = 0.1
    time.sleep(sleep_timer)

    # Ball moves
    ball.move()

    # Detect the Ceiling and bounce
    if ball.check_top_wall():
        ball.bounce_y()

    # Detect the left wall and bounce
    if ball.check_left_wall():
        ball.bounce_x()

    # Detect the right wall and bounce
    if ball.check_right_wall():
        ball.bounce_x()

    # Detect ball misses the Paddle and then end Game, Reset ball
    if ball.check_ball_missed():
        ball.reset_ball()
        scoreboard.gameover()
        screen.update()
        game_is_on = False

    # Detect collision with bricks
    for brick in bricks.all_bricks:
        if brick.distance(ball) < 30:
            scoreboard.point()
            brick.hideturtle()
            bricks.all_bricks.remove(brick)

    # Detect collision with paddle
    if paddle.distance(ball) < 20 and ball.ycor() > -250:
        print(ball.ycor())
        ball.bounce_y()

screen.exitonclick()