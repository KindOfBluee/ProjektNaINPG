import pygame, sys
from random import randrange as rand


class Tetrimino:
    T = [[1, 1, 1],
         [0, 1, 0]]
    L = [[0, 0, 1],
         [1, 1, 1]]
    J = [[1, 0, 0],
         [1, 1, 1]]
    S = [[0, 1, 1],
         [1, 1, 0]]
    Z = [[1, 1, 0],
         [0, 1, 1]]
    I = [[6, 6, 6, 6]]
    O = [[7, 7],
         [7, 7]]

def rotate_clockwise(shape):
    return [[shape[x][y]
             for y in range(len(shape))]
            for x in range(len(shape[0]) -1, -1, -1)]

def check_collision(board, shape, offset):
    x_off, y_off = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            try:
                if cell and board[y+y_off][x+x_off]:
                    return True
            except IndexError:
                return True
    return False
def join_matrix(mat1, mat2, mat2_off):
    x_off, y_off = mat2_off
    for y, row in enumerate(mat2):
        for x, val in enumerate(row):
            mat1[y+y_off-1][x+x_off] +=val
    return mat1

