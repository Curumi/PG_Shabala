import pygame as pg
from random import choice

from pygame.gfxdraw import rectangle

from all_colors import *
pg.init()

size = (1280, 720)
screen = pg.display.set_mode(size)
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)

COLORS = [BLACK, WHITE, RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, GRAY, ORANGE, 
          PINK, BROWN, PURPLE, LIME, NAVY, OLIVE, MAROON, TEAL, SILVER, GOLD]

rectangles = []  # This will store tuples of (rect, color, filled)
RECTANGLE_COLOR = (255, 0, 0)
top_left = (0, 0)
current_size = (0, 0)  # Renamed from 'size' to avoid conflict with screen size
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
                # Fill all rectangles when space is pressed
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
            rectangles.append((rect, color, False))  # Added 'filled' flag
            dragging = False

        elif event.type == pg.MOUSEMOTION and dragging:
            right_bottom = event.pos
            current_size = (right_bottom[0] - top_left[0],
                           right_bottom[1] - top_left[1])

    screen.fill(BACKGROUND)
    
    # Draw current rectangle being dragged
    if dragging:
        pg.draw.rect(screen, RECTANGLE_COLOR, (top_left, current_size), 1)
    
    # Draw all rectangles
    for rect, color, filled in rectangles:
        if filled:
            pg.draw.rect(screen, color, rect)  # Filled rectangle
        else:
            pg.draw.rect(screen, color, rect, 1)  # Outline only
    
    pg.display.flip()
    clock.tick(FPS)

pg.quit()
