import pygame as pg
from all_colors import *
pg.init()

size = (1280, 720)
screen = pg.display.set_mode(size)
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)

rect1 = pg.Rect(100, 100, 200, 150)
rect2 = pg.Rect(250, 150, 200, 150)


rect3 = pg.Rect(500, 100, 200, 150)
rect4 = pg.Rect(600, 300, 200, 150)

width = 5

def collision(rect, other_rect):
    if rect.colliderect(other_rect):
        pg.draw.rect(screen, RED, rect, width)
        pg.draw.rect(screen, RED, other_rect, width)
    else:
        pg.draw.rect(screen, BLUE, rect, width)
        pg.draw.rect(screen, BLUE, other_rect, width)

collision(rect1, rect2)
collision(rect3, rect4)



FPS = 60
clock = pg.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False





    #screen.fill(BACKGROUND)
    pg.display.flip()
    clock.tick(FPS)

pg.quit()