import pygame as pg
from random import choice


from all_colors import *
pg.init()

size = (1280, 720)
screen = pg.display.set_mode(size)
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)

COLORS = [BLACK, WHITE, RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, GRAY, ORANGE, 
          PINK, BROWN, PURPLE, LIME, NAVY, OLIVE, MAROON, TEAL, SILVER, GOLD]

rectangles = []
RECTANGLE_COLOR = (255, 0, 0)
top_left = (0, 0)
current_size = (0, 0)
dragging = False

FPS = 60
clock = pg.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:

                rectangles = [(rect, color, True) for rect, color, filled in rectangles]

        elif event.type == pg.MOUSEBUTTONDOWN:
            top_left = event.pos
            current_size = 0, 0
            dragging = True

        elif event.type == pg.MOUSEBUTTONUP and dragging:
            right_bottom = event.pos
            current_size = (right_bottom[0] - top_left[0],
                          right_bottom[1] - top_left[1])
            rect = pg.Rect(top_left, current_size)
            color = choice(COLORS)
            rectangles.append((rect, color, False))
            dragging = False

        elif event.type == pg.MOUSEMOTION and dragging:
            right_bottom = event.pos
            current_size = (right_bottom[0] - top_left[0],
                           right_bottom[1] - top_left[1])

    screen.fill(BACKGROUND)
    

    if dragging:
        pg.draw.rect(screen, RECTANGLE_COLOR, (top_left, current_size), 1)
    

    for rect, color, filled in rectangles:
        if filled:
            pg.draw.rect(screen, color, rect)
        else:
            pg.draw.rect(screen, color, rect, 1)
    
    pg.display.flip()
    clock.tick(FPS)

pg.quit()
