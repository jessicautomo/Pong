from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        #self.shapesize(5,5)
        self.speed("fastest")

    def bounce(self):
        heading = 180 - self.heading()
        self.setheading(heading)

    def random_direction_left(self):
        heading = random.randint(100,260)
        self.setheading(heading)

    def random_direction_right(self):
        heading = random.randint(-80,80)
        self.setheading(heading)
