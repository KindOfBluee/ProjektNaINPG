import pygame, sys
from random import randrange as rand


class Tetrimino:
    shapes = [
        [[1, 1, 1],
         [0, 1, 0]],#  T
        [[0, 0, 1],
         [1, 1, 1]],#  L
        [[1, 0, 0],
         [1, 1, 1]],#  J
        [[0, 1, 1],
         [1, 1, 0]],#  S
        [[1, 1, 0],
         [0, 1, 1]],#  Z
        [[6, 6, 6, 6]],#  I
        [[7, 7],
         [7, 7]]]#  O

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

def clear_row(board, row, cols):
    del board[row]
    return [[ 0 for i in range(cols)]] + board

def join_matrix(mat1, mat2, mat2_off):
    x_off, y_off = mat2_off
    for y, row in enumerate(mat2):
        for x, val in enumerate(row):
            mat1[y+y_off-1][x+x_off] +=val
    return mat1

class Board:
    dim = []
    def set_dim(cols, rows):
        dim = [[ 0 for x in range(cols) ] for y in range(rows)]
        dim += [[ 1 for x in range(cols)]]
        return dim
