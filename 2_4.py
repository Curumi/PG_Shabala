from random import *
from all_colors import *
import pygame as pg
from pygame.constants import *

from all_colors import *

pg.init()

size = (1280, 720)
screen = pg.display.set_mode(size)
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)

COLORS = [BLACK, WHITE, RED, GREEN, YELLOW, CYAN, MAGENTA, GRAY,
          ORANGE, PINK, BROWN, PURPLE, LIME, NAVY, OLIVE, MAROON, TEAL, GOLD]

initial_size = 200
FPS = 60
clock = pg.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    size = initial_size
    for i in range(18):
        rect = pg.Rect(0,0, size, size)






    pg.display.flip()
    clock.tick(FPS)

pg.quit()