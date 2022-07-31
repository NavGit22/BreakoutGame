from turtle import Turtle
import random

COLORS = ['red','orange','yellow','green','blue','purple','pink']


class Bricks:
    def __init__(self):
        self.all_bricks = []

    def create_bricks(self):
        ycor = 10
        while ycor < 200:
            xcor = -360
            while xcor < -360 or xcor < 360:
                brick = Turtle('square')
                brick.shapesize(stretch_wid=1, stretch_len=2)
                brick.penup()
                brick.color(random.choice(COLORS))
                brick.goto(xcor, ycor)
                xcor = xcor + 45
                self.all_bricks.append(brick)
            ycor = ycor + 25






