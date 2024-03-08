from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, name, position):
        super().__init__()
        self.name = name
        self.color("orange")
        self.penup()
        self.goto(position)
        self.pendown()
        self.write(f"{name}:\n0",align="center",font=("default",15,"normal"))
        self.hideturtle()

    def refresh(self, score):
        self.clear()
        self.write(f"{self.name}:\n{score}",align="center",font=("default",15,"normal"))

    def game_over(self, winner):
        self.color("#fff8e7")
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.write(f"GAME OVER\n{winner} wins!", align="center", font=("default", 30, "normal"))
        self.hideturtle()
