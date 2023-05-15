from enum import Enum
import pygame
import os

class Global(Enum):

    # window
    WIN_WIDTH = 600
    WIN_HEIGHT = 800

    PIPE_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","media/pipe.png")))
    BASE_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "media/base.png")))
    BACKGROUND_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "media/bg.png")))

class Bird(Enum):

    # fixed attributes
    MAX_ROTATION = 25
    ROTATION_VELOCITY = 20
    ANIMATION_TIME = 5

    # media load
    Bird_IMAGE_1 = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "media/bird1.png")))
    Bird_IMAGE_2 = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "media/bird2.png")))
    Bird_IMAGE_3 = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "media/bird3.png")))