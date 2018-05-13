from random import *
import  pygame

class Gameover:
    def __init__(self, width, height, score, bg_color=(255, 255, 255), font_color=(0, 0, 0)):
        self.width = width
        self.height = height
        self.score = score
        self.pressContinue - 0
        self.bg_color = bg_color
        self.font_color = font_color

    def draw_gameover(self, screen):
        pygame.draw.rect(screen, self.bg_color, (50, 50, self.width - 100, self.height - 100), 0)

        tetris_font = pygame.font.Font(pygame.font.get_default_font(), 32)
        tetris_font.set_bold(1)

        label_1 = tetris_font.render("GAMEOVER", 1, self.font_color)
        label_1_rect = label_1.get_rect()
        label_1_rect.center = (150, 150)

        tetris_font = pygame.font.SysFont("monospace", 12)
        label_2 = tetris_font.render("SCORE:\n%i" % self.score, 1, self.font_color)
        label_2_rect = label_2.get_rect()
        label_2_rect.center = (150, 280)

        screen.blit(label_1, label_1_rect)
        screen.blit(label_2, label_2_rect)

    def press_continue(self, screen):
        tetris_font = pygame.font.SysFont("monospace", 12)

        label_1 = tetris_font.render("PRESS ANY BUTTON TO CONTINUE", 1, self.font_color)
        label_1_rect = label_1.get_rect()
        label_1_rect.center = (150, 350)

        screen.blit(label_1, label_1_rect)