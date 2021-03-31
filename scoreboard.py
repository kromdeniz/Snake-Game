from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 16, "bold", )

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.sety(275)
        self.update()


    def update(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over :(", align=ALIGNMENT, font=FONT)