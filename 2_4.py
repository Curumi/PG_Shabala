from random import *
from all_colors import *
import pygame as pg
from pygame.constants import *

from all_colors import BLACK

pg.init()

size = (1280, 720)
screen = pg.display.set_mode(size)
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)
x = 0
y = 0
rect_size = 200
colors = [RED, BLACK]

# rect1 = pg.Rect(x, y, rect_size, rect_size)
# rect1.center = (screen.get_width()//2, screen.get_height()//2)
# pg.draw.rect(screen, BLACK, rect1)
#
# rect2 = pg.Rect(x, y, rect_size//2, rect_size//2)
# rect2.center = (screen.get_width()//2, screen.get_height()//2)
# pg.draw.rect(screen, RED, rect2)

for i in range(18):
    rect1 = pg.Rect(x, y, rect_size, rect_size)
    rect1.center = (screen.get_width()//2, screen.get_height()//2)
    pg.draw.rect(screen, BLACK, rect1)


FPS = 60
clock = pg.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False




    pg.display.flip()
    clock.tick(FPS)

pg.quit()