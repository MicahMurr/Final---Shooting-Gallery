import turtle
import random
from turtle import *


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("white")
screen.title("Shooting Gallery")
screen.tracer(0)


block_list = []
game_active = True


class Player(Turtle):
   def __init__(self, color_name, start_x, start_y):
       super().__init__()
       self.shape("triangle")
       self.color(color_name)
       self.pu()
       self.goto(start_x, start_y)
       self.setheading(90)
       self.rounds = []
       self.score = 0


   def turn_left(self):
       new_heading = self.heading() + 10
       if 15 <= new_heading <= 165:
           self.setheading(new_heading)


   def turn_right(self):
       new_heading = self.heading() - 10
       if 15 <= new_heading <= 165:
           self.setheading(new_heading)
