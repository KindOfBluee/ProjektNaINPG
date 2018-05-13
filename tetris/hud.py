from random import *
import pygame

class Hud:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.score = 0

    def draw_hud(self, screen):
        border_color = (100, 0, 0)
        pygame.draw.rect(screen, border_color, (self.width/3*2, 0, 2, self.height))
        pygame.draw.rect(screen, border_color, (self.width / 3 * 2, self.height/4, self.width, 0))
        pygame.draw.rect(screen, border_color, (self.width / 3 * 2, self.height/4*3, self.width, 0))