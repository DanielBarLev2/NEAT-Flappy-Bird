import pygame.transform

from src.constants import constants

class Bird:

    images_list = [constants.Bird.Bird_IMAGE_1.value,
                   constants.Bird.Bird_IMAGE_2.value,
                   constants.Bird.Bird_IMAGE_3.value]


    def __init__(self, x, y):
        """
        default constructor of the class
        :param x: starting x coordinate on the screen
        :param y: starting y coordinate on the screen
        """
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.image_count = 0
        self.image = self.images_list[0]

    def jump(self):
        """
        Alter the birds velocity to mimic jumping
        """
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y


    def move(self):
        """
        Moves the bird across the screen by calculating the current position via physics implementation
        """
        self.tick_count += 1

        # physics formula to calculate distance
        distance = self.vel * self.tick_count + 1.5 * self.tick_count ** 2

        # terminal velocity
        if distance >= 16:
            distance = 16
        elif distance < 0:
            distance -= 2

        self.y = self.y + distance

        # rotation handling
        if distance < 0 or self.y < self.height + 50:
            if self.tilt < constants.Bird.MAX_ROTATION.value:
                self.tilt = constants.Bird.MAX_ROTATION.value
        else:
            if self.tilt > -90:
                self.tilt -= constants.Bird.ROTATION_VELOCITY


    def draw(self, win):
        """
        Animate the bird in sequence of five using three images.
        The function determines the right position by animation time circle.
        In addition, rotate and tilt the image respectively
        :param win:
        """
        self.image_count += 1

        if self.image_count < constants.Bird.ANIMATION_TIME.value:
            self.image = self.images_list[0]

        elif self.image_count < constants.Bird.ANIMATION_TIME.value * 2:
            self.image = self.images_list[1]

        elif self.image_count < constants.Bird.ANIMATION_TIME.value * 3:
            self.image = self.images_list[2]

        elif self.image_count < constants.Bird.ANIMATION_TIME.value * 4:
            self.image = self.images_list[1]

        elif self.image_count < constants.Bird.ANIMATION_TIME.value * 4 + 1:
            self.image = self.images_list[0]
            self.image_count = 0

        # cancel wing movement when diving
        if self.tilt <= -80:
            self.image = self.images_list[1]
            self.image_count = constants.Bird.ANIMATION_TIME.value * 2

        # rotates the image:
        rotated_image = pygame.transform.rotate(self.image, self.tilt)
        new_rec = rotated_image.get_rect(center=self.image.get_rect(toplef= (self.x, self.y)).center)
        win.blit(rotated_image, new_rec.topleft)


    def get_mask(self):
        """
        Handles collisions

        *** not implemented ***
        :return:
        """
        return pygame.mask.from_surface(self.image)
