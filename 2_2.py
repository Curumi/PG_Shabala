
from all_colors import *
import pygame as pg
pg.init()

size = (1280, 720)
screen = pg.display.set_mode(size)
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)


width, height = 100,100
x, y = 50,50
color = RED
speed = 5



FPS = 60
clock = pg.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                y -= speed
                if y < 0:
                    y = 0

            elif event.key == pg.K_DOWN:
                if event.key == pg.K_DOWN:
                    y -= speed
                    if y > 620:
                        y = 620

            elif event.key == pg.K_LEFT:
                if event.key == pg.K_LEFT:
                    x -= speed
                    if x < 0:
                        x = 0

            elif event.key == pg.K_RIGHT:
                if event.key == pg.K_RIGHT:
                    x += speed
                    if x > 1100:
                        x = 1100
            else:
                print(f'Нажали клавишу {event.key}')

        # elif event.type == pg.KEYUP:
        #     if event.key == pg.K_UP:
        #         print('Отпустили клавишу вверх ')
        #     elif event.key == pg.K_DOWN:
        #         print('Отпустили клавишу вниз ')
        #     elif event.key == pg.K_LEFT:
        #         print('Отпустили клавишу влево ')
        #     elif event.key == pg.K_RIGHT:
        #         print('Отпустили клавишу вправо ')
        #     else:
        #         print('Отпустили клавишу', event.key)



    screen.fill(BACKGROUND)
    pg.draw.rect(screen, color, (x, y, width, height))
    pg.display.flip()
    clock.tick(FPS)

pg.quit()