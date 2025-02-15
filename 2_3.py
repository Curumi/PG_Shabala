from random import *
from all_colors import *
import pygame as pg
from pygame.constants import *
pg.init()

size = (1280, 720)
screen = pg.display.set_mode(size)
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)

rect = pygame.Rect(0,100, 200, 150)
speed = 5



FPS = 60
clock = pg.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    rect.x += speed
    if rect.x > screen.get_width():
        rect.x = -rect.width

    screen.fill(BACKGROUND)
    pg.draw.rect(screen,BLUE, rect)
    pg.display.flip()
    clock.tick(FPS)

pg.quit()