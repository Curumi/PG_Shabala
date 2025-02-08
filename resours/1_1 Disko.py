from all_colors import *
import pygame as pg
import random
pg.init()


# pg.mixer.init()
# pg.mixer.music.load('resources/MGE')
# pg.mixer.music.play(-1)

size = (0,0)
pg.display.set_caption('MGE_disko')
screen = pg.display.set_mode(size, pg.FULLSCREEN)
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)


time = 0

COLORS = [BLACK, WHITE,RED, GREEN,BLUE, YELLOW, CYAN,MAGENTA,GRAY, ORANGE, PINK, BROWN, PURPLE, LIME, NAVY, OLIVE, MAROON, TEAL,SILVER, GOLD]


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill(random.choice(COLORS))
    pg.display.flip()
    pg.time.delay(random.randint(200, 600))



pg.quit()