from random import *
import pygame

class Menu:
    def __init__(self, width, height, bg_color, font_color):
        self.width = width
        self.height = height
        self.demo = 0
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

        label_1 = tetris_font.render("TETRIS", self.font_color)
        label_1_rect = label_1.get_rect()
        label_1_rect.center(150, 100)

        screen.blit(label_1, label_1_rect)

    def draw_info(self, screen):
        pygame.draw.rect(screen, self.bg_color, (50, 50, self.width - 100, self.height - 100))

        tetris_font = pygame.font.Font(pygame.font.get_default_font(), 32)
        tetris_font.set_bold(1)

        label_1 = tetris_font.render("INFO", self.font_color)
        label_1_rect = label_1.get_rect()
        label_1_rect.center(150, 100)

        tetris_font = pygame.font.SysFont("monospace", 12)

        label_2 = tetris_font.render("> LEFT\n< RIGHT\nV DOWN\nSPACE DROP\n^ ROTATE\nPRESS ANY BUTTON TO CONTINUE", 1, self.font_color)

        label_2_rect = label_2.get_rect()
        label_2_rect.center = (150, 200)

    def update_menu(self, screen):
        tetris_font = pygame.font.Font(pygame.font.get_default_font(), 32)
        tetris_font.set_bold(0)

        bg_singlePlayer = (255*(1-self.singlePlayer), 255*(1-self.singlePlayer), 255*(1-self.singlePlayer))
        bg_demo = (255*(1-self.demo), 255*(1-self.demo), 255*(1-self.demo))
        bg_info = (255*(1-self.info), 255*(1-self.info), 255*(1-self.info))

        font_singlePlayer = (255*(1-self.singlePlayer), 255*(1-self.singlePlayer), 255*(1-self.singlePlayer))
        font_demo = (255*(1-self.demo), 255*(1-self.demo), 255*(1-self.demo))
        font_info = (255*(1-self.info), 255*(1-self.info), 255*(1-self.info))

        pygame.draw.rect(screen, bg_singlePlayer, (90, 180, 120, 20), 0)
        label_2 = tetris_font.render("1 PLAYER", 1, font_singlePlayer)
        label_2_rect = label_2.get_rect()
        label_2_rect.center = (150, 190)

        pygame.draw.rect(screen, bg_demo, (90, 240, 120, 20), 0)
        label_3 = tetris_font.render("DEMO", 1, font_demo)
        label_3_rect = label_3.get_rect()
        label_3_rect.center = (150, 250)

        pygame.draw.rect(screen, bg_info, (90, 300, 120, 20), 0)
        label_4 = tetris_font.render("INFO", 1, font_info)
        label_4_rect = label_4.get_rect()
        label_4_rect.center = (150, 310)

        screen.blit(label_2, label_2_rect)
        screen.blit(label_3, label_3_rect)
        screen.blit(label_4, label_4_rect)

    def move_cursor(self, directon):
        if self.demo:
            if self.direction == 1:
                self.demo = 0
                self.singlePlayer = 1
            elif directon == -1:
                self.demo = 0
                self.info = 1
        if self.singlePlayer:
            if self.direction == 1:
                self.singlePlayer = 0
                self.info = 1
            elif directon == -1:
                self.singlePlayer = 0
                self.demo = 1
        if self.info:
            if self.direction == 1:
                self.info = 0
                self.demo = 1
            elif directon == -1:
                self.info = 0
                self.singlePlayer = 1

    def reset(self):
        self.demo = 0
        self.singlePlayer = 1
        self.info = 0
        self.start = 0
        self.infoDone = 0