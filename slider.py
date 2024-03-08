from turtle import Turtle

class Slider(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.setheading(90)
        self.color("white")
        self.width(5)
        self.shapesize(stretch_wid=3)
        self.penup()
        self.goto(position)

    def up(self):
        if self.ycor() < 265:
            y = self.ycor()
            self.sety(y + 15)

    def down(self):
        if self.ycor() > -265:
            y = self.ycor()
            self.sety(y - 15)