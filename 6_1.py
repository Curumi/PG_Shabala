import math
import pygame as pg
pg.init()

size = (1280, 720)
screen = pg.display.set_mode(size)
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)
FPS = 60

BUTTON_COLOR = (0,191,255)
HOVER_COLOR = (0,140,255)
CLICK_COLOR = (0,50,255)

BUTTON_RADIUS = 50
BUTTON_CENTER = [size[0]//2, size [1]//2]

hovering = False
clicking = False

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

clock = pg.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.MOUSEMOTION:
            if (distance(event.pos, BUTTON_CENTER)
                    < BUTTON_RADIUS):
                hovering = True
            else:
                hovering    = False

            if clicking:
                BUTTON_CENTER[0] = event.pos[0]
                BUTTON_CENTER[1] = event.pos[1]


        elif event.type == pg.MOUSEBUTTONDOWN:
            if (event.button == 3 and distance(event.pos,BUTTON_CENTER)
                    < BUTTON_RADIUS):
                clicking = True

        elif event.type == pg.MOUSEBUTTONUP:
            clicking = False



    screen.fill(BACKGROUND)

    if clicking:
        button_color = CLICK_COLOR
    elif hovering:
        button_color = HOVER_COLOR
    else:
        button_color = BUTTON_COLOR

    pg.draw.circle(screen, button_color,BUTTON_CENTER, BUTTON_RADIUS)
    pg.display.flip()
    clock.tick(FPS)

pg.quit()