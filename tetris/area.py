from random import *
import pygame


class Area:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = []
        self.lines_cleared = 0
        self.score = 0
        self.level = 1

        array_build = []
        for row in range(int(self.height/20)):
            for column in range(int(self.height/20)):
                array_build.append(0)
            self.area.append(array_build)
            array_build = []

    def matrix(self):
        return self.area

    def draw_area(self, tetrino, matrix, screen):
        self.check_state(tetrino, matrix)
        solid_color = (70, 70, 70)
        solid = pygame.image.load("outside.png").convert()
        solid.fill(solid_color, (1, 1, 18, 18))

        for row, row_items in enumerate(matrix):
            for column, item in enumerate(row_items):
                x, y = column, row
                if item == 1:
                    screen.blit(solid, (x*20, y*20))

    def draw_next(self, tetrino, screen):
        if tetrino.id == 0:
            for index, item in enumerate(tetrino.x):
                screen.blit(tetrino.block, ((tetrino.x[index]*20), (tetrino.y[index]*20+15)))
        elif tetrino.id == 1:
            for index, item in enumerate(tetrino.x):
                screen.blit(tetrino.block, ((tetrino.x[index]*20-10), (tetrino.y[index]*20+40)))
        elif tetrino.id == 2:
            for index, item in enumerate(tetrino.x):
                screen.blit(tetrino.block, ((tetrino.x[index] * 20), (tetrino.y[index] * 20 + 35)))
        elif tetrino.id == 3:
            for index, item in enumerate(tetrino.x):
                screen.blit(tetrino.block, ((tetrino.x[index] * 20 - 10), (tetrino.y[index] * 20 + 25)))
        elif tetrino.id == 4:
            for index, item in enumerate(tetrino.x):
                screen.blit(tetrino.block, ((tetrino.x[index] * 20 + 10), (tetrino.y[index] * 20 + 25)))
        elif tetrino.id == 5:
            for index, item in enumerate(tetrino.x):
                screen.blit(tetrino.block, ((tetrino.x[index] * 20), (tetrino.y[index] * 20 + 30)))
        elif tetrino.id == 6:
            for index, item in enumerate(tetrino.x):
                screen.blit(tetrino.block, ((tetrino.x[index] * 20), (tetrino.y[index] * 20 + 30)))

    def check_state(self, tetrino, matrix):
        if tetrino.state == 1:
            for ind, i in enumerate(tetrino.x):
                if matrix[tetrino.y[ind]][tetrino.x[ind]] == 0:
                    matrix[tetrino.y[ind]][tetrino.x[ind]] = 1
        old_lines_cleared = self.lines_cleared
        count = 0
        update_score = 0
        for row, row_items in enumerate(matrix):
            if sum(row_items) == 10:
                matrix.pop(row)
                matrix.reverse()
                matrix.append([0]*10)
                matrix.reverse()
                self.lines_cleared += 1
                count += 1
                update_score += 1

        if update_score == 1:
            self.score += (self.lines_cleared - old_lines_cleared) * count * 100 * self.level
            if self.lines_cleared % 10 == 0:
                self.level += 1

    def print_game_info(self, screen):
        font = pygame.font.SysFont("monospace", 12)
        font_color = (100, 100, 100)

        label_1 = font.render("LINES: %i" % self.lines_cleared, 1, font_color)
        label_1_rect = label_1.get_rect()
        label_1_rect.center = (236, self.height /8*7 - 40)

        label_2 = font.render("SCORE: %i" % self.score, 1, font_color)
        label_2_rect = label_2.get_rect()
        label_2_rect.center = (236, self.height/8*7 - 25)

        label_3 = font.render("LEVEL: %i" % self.level, 1, font_color)
        label_3_rect = label_3.get_rect()
        label_3_rect.center = (236, self.height / 8 * 7 - 10)

        screen.blit(label_1, label_1_rect)
        screen.blit(label_2, label_2_rect)
        screen.blit(label_3, label_3_rect)