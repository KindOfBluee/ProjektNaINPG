import pygame, sys, os, core
from pygame.locals import *
from core import *

cols = 10
rows = 22
cell_size = 18
max_fps = 30


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

class Tetris(object):
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(250, 25)

        self.width = cell_size * (cols + 6)
        self.height = cell_size * rows
        self.rlim = cell_size * cols

        self.bg_grid = [[8 if x % 2 - -y % 2 else 0 for x in range(cols)] for y in range(rows)]

        self.default_font = pygame.font.Font(pygame.font.get_default_font(), 12)
        self.screen = pygame.display.set_mode((width, height))
        pygame.event.set_blocked(pygame.MOUSEMOTION)
        self.next_stone = Tetrimino.shapes[rand(len(Tetrimino.shapes))]

        self.init_game()

    def new_stone(self):
        self.stone = self.next_stone[:]
        self.next_stone = Tetrimino.shapes[rand(len(Tetrimino.shapes))]
        stone_x = int(cols / 2 - len(self.stone[0])/2)
        stone_y = 0

        if check_collision(board, self.stone, (stone_x, stone_y)):
            self.gameover = True


    def init_game(self):
        self.board = Board.set_dim(cols, rows)
        self.next_stone()
        self.level = 1
        self.score = 0
        self.lines = 0
        pygame.time.set_timer(pygame.USEREVENT+1, 1000)

    def display_msg(self, msg, topleft):
        x, y = topleft
        for line in msg.splitlines():
            self.screen.blit(
                self.default_font.render(
                    line,
                    False,
                    (255, 255, 255),
                    (0, 0, 0),
                ),
            ((x,y)))
            y+-14