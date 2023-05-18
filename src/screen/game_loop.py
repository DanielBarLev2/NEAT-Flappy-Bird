from src.constants import constants
from src.Classes import Bird, Base, Pipe
import pygame



def draw_window(win, bird, pipes, base, score):

    win.blit(constants.Screen.BACKGROUND_IMAGE.value, (0, 0))

    for pip in pipes:
        pip.draw(win)

    base.draw(win)

    bird.draw(win)

    test = constants.Screen.FONT.value.render(f'Score {score}', 1, (255,255,255))
    win.blit(test, (constants.Screen.WIN_WIDTH.value - 10 - test.get_width(), 10))
    pygame.display.update()

def run():

    win = pygame.display.set_mode((constants.Screen.WIN_WIDTH.value, constants.Screen.WIN_HEIGHT.value))
    bird = Bird.Bird(230, 250)
    base = Base.Base(730)
    pipes: list = []

    clock = pygame.time.Clock()

    score = 0
    pipe_distance = 600
    top_margin = 50
    bottom_margin = 450

    add_pipe = True
    running = True

    while running:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # bird.move()

        delete_list = []

        for pipe in pipes:
            if pipe.collide(bird):
                pass

            if pipe.x + pipe.pipe_top.get_width() < 0:
                delete_list.append(pipe)

            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe = True

            pipe.move()

        if add_pipe:
            score += 1
            pipes.append(Pipe.Pipe(pipe_distance, top_margin, bottom_margin))
            add_pipe = False

        for d in delete_list:
            pipes.remove(d)

        if bird.y + bird.image.get_height() >= 730:
            pass

        base.move()

        draw_window(win, bird, pipes, base, score)

    pygame.quit()
    quit()