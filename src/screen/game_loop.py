from src.constants import constants
from src.Classes import Bird
import pygame
import random
import time
import neat
import os

def draw_window(win, bird):
    """

    :param win:
    :param bird:
    :return:
    """
    win.blit(constants.Constants.BACKGROUND_IMAGE.value, (0, 0))

    bird.draw(win)

    pygame.display.update()

def run():

    win = pygame.display.set_mode((constants.Constants.WIN_WIDTH.value, constants.Constants.WIN_HEIGHT.value))
    bird = Bird.Bird(200, 200)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_window(win, bird)

    pygame.quit()
    quit()