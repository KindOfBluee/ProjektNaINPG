"""Pong, classic arcade game.
Exercises
1. Change the colors.
2. What is the frame rate? Make it faster or slower.
3. Change the speed of the ball.
4. Change the size of the paddles.
5. Change how the ball bounces off walls.
6. How would you add a computer player?
6. Add a second ball.
"""

from random import choice, random
from turtle import *
from freegames import vector

def value():
    "Randomly generate value between (-5, -3) or (3, 5)."
    return (3 + random() * 2) * choice([1, -1])

ball = vector(0, 0)
aim = vector(value(), value())
state = {1: 0, 2: 0}

def move(player, change):
    "Move player position by change."
    state[player] += change

def rectangle(x, y, width, height):
    "Draw rectangle at (x, y) with given width and height."
    up()
    goto(x, y)
    down()
    begin_fill()
    for count in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()
def draw():
    "Draw game and move pong ball."
    clear()
    rectangle(-200, state[1], 10, 50)
    rectangle(190, state[2], 10, 50)
