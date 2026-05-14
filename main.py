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


   def fire(self):
       if len(self.rounds) < 5 and game_active:
           new_bullet = Bullet(self)
           self.rounds.append(new_bullet)




class Block(Turtle):
   def __init__(self, xval, yval, is_bomb=False):
       super().__init__()
       self.pu()
       self.shape("square")
       self.is_bomb = is_bomb
       if self.is_bomb:
           self.color_list = ["green"]
           self.hits = 0
       else:
           self.color_list = ["gray", "orange", "red"]
           self.hits = 0
       self.goto(xval, yval)
       self.color(self.color_list[self.hits])
       self.showturtle()


   def delete(self):
       self.hideturtle()
       if self in block_list:
           block_list.remove(self)


   def strike(self, player):
       if self.is_bomb:
           self.detonate(player)
       else:
           self.hits += 1
           if self.hits <= 2:
               self.color(self.color_list[self.hits])
           else:
               player.score += 1
               self.delete()


   def detonate(self, player):
       self.delete()
       player.score += 1
       radius = 60
       for block in list(block_list):
           if self.distance(block) <= radius:
               block.delete()
               player.score += 1





