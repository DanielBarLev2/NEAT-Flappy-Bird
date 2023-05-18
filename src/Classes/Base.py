from src.constants import constants
class Base:

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = constants.Base.WIDTH.value


    def move(self):
        self.x1 -= constants.Base.VEL.value
        self.x2 -= constants.Base.VEL.value

        # cycle through the base
        if self.x1 + constants.Base.WIDTH.value < 0:
            self.x1 = self.x2 + constants.Base.WIDTH.value

        if self.x2 + constants.Base.WIDTH.value < 0:
            self.x2 = self.x1 + constants.Base.WIDTH.value

    def draw(self, win):
        win.blit(constants.Base.IMAGE.value, (self.x1, self.y))
        win.blit(constants.Base.IMAGE.value, (self.x2, self.y))
