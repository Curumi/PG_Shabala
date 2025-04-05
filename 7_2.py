import math

import pygame as pg
from pygame.draw import circle

pg.init()




def distance(pos1, pos2):
    return math.sqrt((pos2[0] - pos1[0]) ** 2
                     + (pos2[1]- pos1[1]) ** 2)


def move_towards(pos1, pos2, min_speed = 1, max_speed = 10):
    x1, y1 = pos1
    x2, y2 = pos2
    dx = x2 - x1
    dy = y2 - y1
    dist = distance(pos1,pos2)

    if dist < min_speed:
        return pos2

    if dist == 0:
        return pos1

    speed = max(min_speed, min(dist / 5, max_speed))

    dx /= dist
    dy /= dist

    x1 += dx * speed
    y1 += dy * speed

    return (x1, y1)





size = (640, 480)
screen = pg.display.set_mode(size)
BACKGROUND = (0, 0, 0)
CIRCLE_COLOR = (255, 255, 255)
CIRCLE_RADIUS = 20
screen.fill(BACKGROUND)

circle_pos = (320,240)
speed = 3

FPS = 60
clock = pg.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    mouse_pos = pg.mouse.get_pos()

    circle_pos = move_towards(circle_pos, mouse_pos, speed)


    screen.fill(BACKGROUND)
    pg.draw.circle(screen, CIRCLE_COLOR, (int(circle_pos[0]), int(circle_pos[1])), CIRCLE_RADIUS)
    pg.display.flip()
    clock.tick(FPS)

pg.quit()
