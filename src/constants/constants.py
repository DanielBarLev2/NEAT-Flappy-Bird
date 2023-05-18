from enum import Enum
import pathlib
import pygame
import os


def get_path(file_name: str) -> str:
    """
    return full path to file.
    :param file_name: name of file and extinction
    :return: full path to file
    """
    path = f'C:\\Users\\danie\\PycharmProjects\\NEAT-Flappy-Bird\\media\\{file_name}'
    path = path.replace(str("\\"), str("/"))
    return path


class Constants(Enum):

    # window
    WIN_WIDTH = 500
    WIN_HEIGHT = 800

    PIPE_IMAGE = pygame.transform.scale2x(pygame.image.load(get_path(file_name="pipe.png")))
    BASE_IMAGE = pygame.transform.scale2x(pygame.image.load(get_path(file_name="base.png")))
    BACKGROUND_IMAGE = pygame.transform.scale2x(pygame.image.load(get_path(file_name="bg.png")))

class Bird(Enum):

    # fixed attributes
    MAX_ROTATION = 25
    ROTATION_VELOCITY = 20
    ANIMATION_TIME = 5

    # media load
    Bird_IMAGE_1 = pygame.transform.scale2x(pygame.image.load(get_path(file_name="bird1.png")))
    Bird_IMAGE_2 = pygame.transform.scale2x(pygame.image.load(get_path(file_name="bird2.png")))
    Bird_IMAGE_3 = pygame.transform.scale2x(pygame.image.load(get_path(file_name="bird3.png")))