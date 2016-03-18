__author__ = 'lenovo'
image_board_filename = "material/board.gif"

import pygame
from pygame.locals import *
from world import *


def process():
    screen = pygame.display.set_mode((377, 417), 0, 32)
    pygame.display.set_caption("Let's play chess!")

    image_board = pygame.image.load(image_board_filename).convert()

    world = World(screen)
    world.start_new_game()

    while True:
        screen.blit(image_board, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                world.answer_mouse(mouse_position)
        world.render()
        pygame.display.update()


