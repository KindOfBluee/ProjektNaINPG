from random import *
import pygame


class Menu:

    def __init__(self, width, height, bg_color, font_color):
        self.width = width
        self.height = height
        self.doublePlayer = 0
        self.singlePlayer = 1
        self.info = 0
        self.start = 0
        self.infoDone = 0
        self.bg_color = bg_color
        self.font_color = font_color

    def draw_menu(self, screen):
        pygame.draw.rect(screen, self.bg_color, (50, 50, self.width - 100, self.height - 100), 0)

        tetris_font = pygame.font.Font(pygame.font.get_default_font(), 32)
        tetris_font.set_bold(1)

        label_1 = tetris_font.render("TETRIS", 1, self.font_color)
        label_1_rect = label_1.get_rect()
        label_1_rect.center = (150, 100)

        screen.blit(label_1, label_1_rect)

    def draw_info(self, screen):
        pygame.draw.rect(screen, self.bg_color, (50, 50, self.width - 100, self.height - 100))

        tetris_font = pygame.font.Font(pygame.font.get_default_font(), 32)
        tetris_font.set_bold(1)

        label_1 = tetris_font.render("INFO", 1, self.font_color)
        label_1_rect = label_1.get_rect()
        label_1_rect.center = (150, 100)

        tetris_font = pygame.font.SysFont("monospace", 12)

        label_2 = tetris_font.render("> LEFT", 1, self.font_color)
        label_2_rect = label_2.get_rect()
        label_2_rect.center = (150, 200)
        label_3 = tetris_font.render("< RIGHT", 1, self.font_color)
        label_3_rect = label_3.get_rect()
        label_3_rect.center = (150, 220)
        label_4 = tetris_font.render("V DOWN", 1, self.font_color)
        label_4_rect = label_4.get_rect()
        label_4_rect.center = (150, 240)
        label_5 = tetris_font.render("SPACE DROP", 1, self.font_color)
        label_5_rect = label_5.get_rect()
        label_5_rect.center = (150, 260)
        label_6 = tetris_font.render("^ ROTATE", 1, self.font_color)
        label_6_rect = label_6.get_rect()
        label_6_rect.center = (150, 280)
        label_7 = tetris_font.render("PRESS ANY BUTTON TO CONTINUE", 1, self.font_color)
        label_7_rect = label_7.get_rect()
        label_7_rect.center = (150, 300)

        screen.blit(label_1, label_1_rect)
        screen.blit(label_2, label_2_rect)
        screen.blit(label_3, label_3_rect)
        screen.blit(label_4, label_4_rect)
        screen.blit(label_5, label_5_rect)
        screen.blit(label_6, label_6_rect)
        screen.blit(label_7, label_7_rect)

    def update_menu(self, screen):
        tetris_font = pygame.font.Font(pygame.font.get_default_font(), 32)
        tetris_font.set_bold(0)

        bg_singlePlayer = (255 * self.singlePlayer, 255 * self.singlePlayer, 255 * self.singlePlayer)
        bg_doublePlayer = (255 * self.doublePlayer, 255 * self.doublePlayer, 255 * self.doublePlayer)
        bg_info = (255 * self.info, 255 * self.info, 255 * self.info)

        font_singlePlayer = (150*(1-self.singlePlayer), 150*(1-self.singlePlayer), 150*(1-self.singlePlayer))
        font_doublePlayer = (150 * (1 - self.doublePlayer), 150 * (1 - self.doublePlayer), 150 * (1 - self.doublePlayer))
        font_info = (150*(1-self.info), 150*(1-self.info), 150*(1-self.info))

        pygame.draw.rect(screen, (255, 255, 255), (90, 180, 120, 20), 0)

        label_2 = tetris_font.render("1 PLAYER", 1, font_singlePlayer)
        label_2_rect = label_2.get_rect()
        label_2_rect.center = (150, 190)

        pygame.draw.rect(screen, (255, 255, 255), (90, 240, 120, 20), 0)
        label_3 = tetris_font.render("2 PLAYERS", 1, font_doublePlayer)
        label_3_rect = label_3.get_rect()
        label_3_rect.center = (150, 250)

        pygame.draw.rect(screen, (255, 255, 255), (90, 300, 120, 20), 0)
        label_4 = tetris_font.render("INFO", 1, font_info)
        label_4_rect = label_4.get_rect()
        label_4_rect.center = (150, 310)

        screen.blit(label_2, label_2_rect)
        screen.blit(label_3, label_3_rect)
        screen.blit(label_4, label_4_rect)

    def move_cursor(self, direction):
        if self.singlePlayer:
            if direction == 1:
                self.singlePlayer = 0
                self.info = 1
            elif direction == -1:
                self.singlePlayer = 0
                self.doublePlayer = 1

        elif self.doublePlayer:
            if direction == 1:
                self.doublePlayer = 0
                self.singlePlayer = 1
            elif direction == -1:
                self.doublePlayer = 0
                self.info = 1

        elif self.info:
            if direction == 1:
                self.info = 0
                self.doublePlayer = 1
            elif direction == -1:
                self.info = 0
                self.singlePlayer = 1

    def reset(self):
        self.doublePlayer = 0
        self.singlePlayer = 1
        self.info = 0
        self.start = 0
        self.infoDone = 0