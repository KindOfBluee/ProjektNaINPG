from random import *
from tetrino import Tetrino
from area import Area
from hud import  Hud
from menu import Menu
from gameover import Gameover
import pygame, sys


class Core:

    def __init__(self, tetrino, area, menu, screen):
        self.tetrino = tetrino
        self.area = area
        self.menu = menu
        self.screen = screen

    def update(self, tetrino, area, menu, screen):
        self.tetrino = tetrino
        self.area = area
        self.menu = menu
        self.screen = screen

    def check_input(self):
        for events in pygame.event.get():

            if events.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_UP:
                    self.tetrino.rotate()

                if events.key == pygame.K_DOWN:
                    self.tetrino.test_y(self.area.matrix())
                    if self.tetrino.collision != 1:
                        self.tetrino.move_down(self.area.matrix())

                if events.key == pygame.K_LEFT:
                    self.tetrino.move_left(self.area.matrix())

                if events.key == pygame.K_RIGHT:
                    self.tetrino.move_right(self.area.matrix())

                if events.key == pygame.K_SPACE:
                    self.tetrino.test_y(self.area.matrix())
                    while self.tetrino.collision != 1:
                        self.tetrino.move_down(self.area.matrix())
                        self.tetrino.draw(self.area.matrix(), self.screen)
                        self.area.draw_area(self.tetrino, self.area.matrix(), self.screen)

        return self.area

    def menu_input(self):
        while not self.menu.start:
            for events in pygame.event.get():

                if events.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if events.type == pygame.KEYDOWN:

                    if events.key == pygame.K_DOWN:
                        self.menu.move_cursor(-1)
                        self.menu.update_menu(self.screen)
                        pygame.display.flip()

                    if events.key == pygame.K_UP:
                        self.menu.move_cursor(1)
                        self.menu.update_menu(self.screen)
                        pygame.display.flip()

                    if events.key == pygame.K_RETURN:
                        self.menu.start = 1
