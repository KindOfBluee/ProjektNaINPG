from random import *
from tetrino import Tetrino
from area import Area
from hud import  Hud
from menu import Menu
from gameover import Gameover
from core import Core
import pygame, sys


pygame.init()

size = width, height = 300, 440

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('TETRIS')
pygame.key.set_repeat(75)

while 1:
    area = Area(width - 100, height)

    tetrino_queue = []

    for i in range(5):
        tetrino_queue.append(randint(0, 6))

    tetrino_color = (randint(1, 255), randint(1, 255), randint(1, 255))

    tetrino = Tetrino(tetrino_color, tetrino_queue[0])

    hud = Hud(width, height)
    gameOver = Gameover(width, height, area.score)

    screen.fill((0, 0, 0))
    hud.draw_hud(screen)
    menu = Menu(width, height, (255, 255, 255), (0, 0, 0))
    menu.draw_menu(screen)
    menu.update_menu(screen)
    pygame.display.flip()
    core = Core(tetrino, area, menu, screen)
    core.menu_input()

    init = 1000
    start_time = pygame.time.get_ticks()

    while menu.singlePlayer and tetrino.game_state:
        core.check_input()
        time = (pygame.time.get_ticks() - start_time)

        if tetrino.state == 1:
            next_tetrino.deactivate()
            tetrino_queue.pop(0)
            tetrino_queue.append(randint(0, 6))
            tetrino = Tetrino(tetrino_color, tetrino_queue[0], 0, 5, 0)
            tetrino_color = (randint(1, 255), randint(1, 255), randint(1, 255))
            core.update(tetrino, area, menu, screen)

        if init < time:
            tetrino.move_down(area.matrix())
            init += (300 - 10*area.level)
            if init < 100:
                init = 100

        screen.fill((0, 0, 0))
        tetrino.draw(area.matrix(), screen)
        area.draw_area(tetrino, area.matrix(), screen)
        area.print_game_info(screen)
        next_tetrino = Tetrino(tetrino_color, tetrino_queue[1], 0, 12, 0)
        next_tetrino.tetrino_update(area.matrix())
        area.draw_next(next_tetrino, screen)
        hud.draw_hud(screen)
        pygame.display.flip()

    first_loop = 1

    while menu.doublePlayer and tetrino.game_state:
        core.check_input()
        time = pygame.time.get_ticks() - start_time

        if tetrino.state == 1:
            next_tetrino.deactivate()
            tetrino_queue.pop(0)
            tetrino_queue.append(randint(0, 6))
            tetrino = Tetrino(tetrino_color, tetrino_queue[0], 0, 5, 0)
            tetrino_color = (randint(1, 255), randint(1, 255), randint(1, 255))
            core.update(tetrino, area, menu, screen)

        if init < time:
            tetrino.move_down(area.matrix())
            init += 300

        screen.fill((0, 0, 0))
        tetrino.draw(area.matrix(), screen)
        area.draw_area(tetrino, area.matrix(), screen)
        area.print_game_info(screen)
        next_tetrino = Tetrino(tetrino_color, tetrino_queue[1], 0, 12, 0)
        next_tetrino.tetrino_update(area.matrix())
        area.draw_next(next_tetrino, screen)
        hud.draw_hud(screen)
        pygame.display.flip()

    first_loop = 1

    while menu.info and not menu.infoDone:
        menu.draw_info(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                menu.infoDone = 1

    while not menu.info and not gameOver.pressContinue:
        gameOver.get_score(area.score)
        gameOver.draw_gameover(screen)
        gameOver.press_continue(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                gameOver.pressContinue = 1

    menu.reset()
