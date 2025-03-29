import pygame as pg
from random import choice

from pygame.gfxdraw import rectangle

from all_colors import *
pg.init()

size = (1280, 720)
screen = pg.display.set_mode(size)
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)

COLORS = [BLACK, WHITE,RED, GREEN,BLUE, YELLOW, CYAN,MAGENTA,GRAY, ORANGE, PINK, BROWN, PURPLE, LIME, NAVY, OLIVE, MAROON, TEAL,SILVER, GOLD]

rectangles = []

RECTANGLE_COLOR = (255, 0, 0)
top_left = (0, 0)
size = (0, 0)
dragging = False

FPS = 60
clock = pg.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.MOUSEBUTTONDOWN:
            top_left = event.pos
            size = 0, 0
            dragging = True

        elif event.type == pg.MOUSEBUTTONUP and dragging:
            right_bottom = event.pos
            size = (right_bottom[0] - top_left[0],
                    right_bottom[1] - top_left[1])
            rect = pg.Rect(top_left,size)
            color = choice(COLORS)
            rectangles.append((rect, color))
            dragging = False

        elif event.type == pg.MOUSEMOTION and dragging:
            right_bottom = event.pos
            size = (right_bottom[0] - top_left[0],
                    right_bottom[1] - top_left[1])



    screen.fill(BACKGROUND)
    pg.draw.rect(screen, RECTANGLE_COLOR, (top_left, size), 1)
    for rectangle, color in rectangles:
        pg.draw.rect(screen, color, rectangle, 1)
    pg.display.flip()
    clock.tick(FPS)

pg.quit()