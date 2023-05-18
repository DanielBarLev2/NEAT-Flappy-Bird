from src.constants import constants
import random
import pygame

class Pipe:

    def __init__(self, x):
        self.x = x
        self.height = 0
        self.gap = 200
        self.vel = 5

        self.top = 0
        self.bottom = 0
        self.pipe_top = pygame.transform.flip(constants.Pipe.PIPE_IMAGE.value, False, True)
        self.pipe_bottom = constants.Pipe.PIPE_IMAGE.value


    def set_height(self):
        self.height = random.randrange(50, 450)
        self.top = self.height - self.pipe_top.get_height()
        self.bottom = self.height + self.gap


    def move(self):
        self.x -= self.vel


    def draw(self, win):
        win.blit(self.pipe_top, (self.x, self.top))
        win.blit(self.pipe_bottom, (self.x, self.bottom))


    def collide(self, bird, win):
        # getting masks
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.pipe_top)
        bottom_mask = pygame.mask.from_surface(self.pipe_bottom)

        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        bottom_point = bird_mask.overlap(bottom_mask, bottom_offset)
        top_point = bird_mask.overlap(top_mask, top_offset)

        if top_point or bottom_point:
            return True

        return False

