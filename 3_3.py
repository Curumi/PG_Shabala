from all_colors import *
import pygame as pg
pg.init()
import pygame.mixer as mx
pg.mixer.init()

mixer = mx.Sound('resours/Mge.mp3')

size = (1280, 720)
screen = pg.display.set_mode(size)
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)
screen_rect = screen.get_rect()



ship = pg.Rect(300, 200, 50, 100)
ship.right = screen_rect.right
ship.center = screen_rect.center

missile = pg.Rect(50, 50, 10, 10)
missile_left = screen_rect.left
missile.centery = screen_rect.centery

missile_speed_x = 0
missile_speed_y = 0

hp_ship = 1
ship_speed_y = 1

ship_alive = True
missile_alive = True

missile_launched = False



FPS = 60


clock = pg.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and not missile_launched:
                missile_launched = True
                missile_speed_x = 3
                missile_speed_y = 0














    screen.fill(BACKGROUND)
    if ship_alive:
        pg.draw.rect(screen, BLUE, ship)
    if missile_alive:
        pg.draw.rect(screen, RED, missile)

    pg.display.flip()
    clock.tick(FPS)

pg.quit()