from random import *
import pygame, sys, os


class Tetrino:
    def __init__(self, color, id=0, rotation=0, track_x=5, track_y=0):
        self.x = []
        self.y = []
        self.id = id
        self.rotation = rotation
        self.state = 0
        self.collision = 0
        self.game_state = 1
        self.track_x = track_x
        self.track_y = track_y
        self.color = color
        self.block = pygame.image.load("outside.png").convert()
        self.block.fill(self.color, (1, 1, 18, 18))
        self.blockrect = self.block.get_rect()

    def tetrinos(self):
        # I
        if self.id == 0 and self.rotation % 2 == 0:
            self.shape = [
                "00200",
                "00200",
                "00200",
                "00200"
            ]
        elif self.id == 0 and self.rotation % 2 == 1:
            self.shape = [
                "00000",
                "22220",
                "00000",
                "00000"
            ]
        # O
        if self.id == 1:
            self.shape = [
                "00220",
                "00220",
                "00000",
                "00000"
            ]
        # T
        if self.id == 2 and self.rotation % 4 == 0:
            self.shape = [
                "02220",
                "00200",
                "00000",
                "00000"
            ]
        elif self.id == 2 and self.rotation % 4 == 1:
            self.shape = [
                "00200",
                "02200",
                "00200",
                "00000"
            ]
        elif self.id == 2 and self.rotation % 4 == 2:
            self.shape = [
                "00200",
                "02220",
                "00000",
                "00000"
            ]
        elif self.id == 2 and self.rotation % 4 == 3:
            self.shape = [
                "00200",
                "00220",
                "00200",
                "00000"
            ]
        #L
        if self.id == 3 and self.rotation % 4 == 0:
            self.shape = [
                "00200",
                "00200",
                "00220",
                "00000"
            ]
        elif self.id == 3 and self.rotation % 4 == 1:
            self.shape = [
                "00000",
                "02220",
                "02000",
                "00000"
            ]
        elif self.id == 3 and self.rotation % 4 == 2:
            self.shape = [
                "02200",
                "00200",
                "00200",
                "00000"
            ]
        elif self.id == 3 and self.rotation % 4 == 3:
            self.shape = [
                "00020",
                "02220",
                "00000",
                "00000"
            ]
        #J
        if self.id == 4 and self.rotation % 4 == 0:
            self.shape = [
                "00200",
                "00200",
                "02200",
                "00000"
            ]
        elif self.id == 4 and self.rotation % 4 == 1:
            self.shape = [
                "02000",
                "02220",
                "00000",
                "00000"
            ]
        elif self.id == 4 and self.rotation % 4 == 2:
            self.shape = [
                "00220",
                "00200",
                "00200",
                "00000"
            ]
        elif self.id == 4 and self.rotation % 4 == 3:
            self.shape = [
                "00000",
                "02220",
                "00020",
                "00000"
            ]
        #S
        if self.id == 5 and self.rotation % 2 == 0:
            self.shape = [
                "02200",
                "00220",
                "00000",
                "00000"
            ]
        elif self.id == 5 and self.rotation % 2 == 1:
            self.shape = [
                "00020",
                "00220",
                "00200",
                "00000"
            ]
        #Z
        if self.id == 6 and self.rotation % 2 == 0:
            self.shape = [
                "00220",
                "02200",
                "00000",
                "00000"
            ]
        elif self.id == 6 and self.rotation % 2 == 1:
            self.shape = [
                "00200",
                "00220",
                "00020",
                "00000"
            ]

    def tetrino_update(self, matrix):
            self.tetrinos()
            self.x=[]
            self.y=[]
            for row_ind, row in enumerate(self.shape):
                for col_ind, item in enumerate(row):
                    if int(item) == 2:
                        self.y.append(row_ind + self.track_y)
                        self.x.append(col_ind - 2 + self.track_x)
            try:
                for ind, y in enumerate(self.y):
                    if y > 0 and matrix[self.y[ind]][self.x[ind]] == 1 and self.track_x == 5 and self.track_y == 0:
                        self.game_state = 0
                for i in range(3):
                    if sum(matrix[i]) > 0:
                        self.game_state = 0
            except IndexError:
                pass

    def draw(self, matrix, screen):
        self.tetrino_update(matrix)
        self.test_rotate(matrix)
        self.check_bounds()
        for index, item in enumerate(self.x):
            screen.blit(self.block, (self.x[index]*20, self.y[index]*20))

    def rotate(self):
        self.rotation += 1

    def move_down(self, matrix):
        self.test_y(matrix)
        if self.collision == 1:
            self.track_y -= 1
            self.y = [i-1 for i in self.y]
            self.deactivate()
        self.y = [i+1 for i in self.y]
        self.track_y += 1

    def move_left(self, matrix):
        self.test_left(matrix)
        self.track_x -= 1
        self.x = [i - 1 for i in self.x]
        if self.collision == 1:
            self.track_x += 1
            self.x = [i + 1 for i in self.x]
            self.collision = 0

    def move_right(self, matrix):
        self.test_right(matrix)
        self.track_x += 1
        self.x = [i + 1 for i in self.x]
        if self.collision == 1:
            self.track_x -= 1
            self.x = [i-1 for i in self.x]
            self.collision = 0

    def deactivate(self):
        self.state =1

    def check_bounds(self):
        max_y = max(self.y)
        max_x = max(self.x)
        min_x = min(self.x)
        if max_y > 21:
            self.y = [i-(max_y-21) for i in self.y]
            self.track_y += max_y - 21
            self.deactivate()
        if min_x < 0:
            self.x = [i - min_x for i in self.x]
            self.track_x -= min_x
        if max_x > 9:
            self.x = [i - (max_x - 9) for i in self.x]
            self.track_x -= max_x - 9

    def test_y(self, matrix):
        try:
            y_test = [i+1 for i in self.y]
            for ind, i in enumerate(y_test):
                if matrix[y_test[ind]][self.x[ind]] == 1:
                    self.collision = 1
        except IndexError:
            self.collision = 1
            pass

    def test_left(self, matrix):
        try:
            x_test = [i-1 for i in self.x]
            for ind, i in enumerate(x_test):
                if matrix[self.y[ind]][x_test[ind]] == 1:
                    self.collision = 1
        except IndexError:
            pass

    def test_right(self, matrix):
        try:
            x_test = [i+1 for i in self.x]
            for ind, i in enumerate(x_test):
                if matrix[self.y[ind]][x_test[ind]] == 1:
                    self.collision = 1
        except IndexError:
            pass

    def test_rotate(self, matrix):
        try:
            rotation_error = 0
            for ind, coord in enumerate(self.x):
                if matrix[self.y[ind]][self.x[ind]] == 1:
                    rotation_error = 1
            if rotation_error == 1:
                self.rotation -= 1
                self.tetrino_update(matrix)
        except IndexError:
            pass