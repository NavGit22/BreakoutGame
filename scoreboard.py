from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-350, 260)
        self.write(self.score, align='center', font=('courier', 20, 'bold'))

    def point(self):
        self.score += 1
        self.update_scoreboard()

    def gameover(self):
        self.clear()
        self.goto(0, -200)
        text = f"Final Score : {self.score}. GAME OVER"
        self.write(text, align='center', font=('courier', 20, 'normal'))

