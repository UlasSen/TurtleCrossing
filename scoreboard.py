from turtle import Turtle

FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-250,260)
        self.write(f"LEVEL:{self.score}", align="center",font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.score += 1
        self.goto(-250,260)
        self.write(f"LEVEL:{self.score}", align="center",font=FONT)
    
    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)



    
