import pygame, sys, os, core
from pygame.locals import *
from core import *
pygame.init()

colors=[
    (0,0,0),
    (255, 85, 85),
    (100, 200, 115),
    (120, 108, 245),
    (225, 140, 50),
    (50, 120, 52),
    (146, 202, 73),
    (150, 161, 218),
    (35, 35, 35),]

window = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Tetris")


