import pygame as pg
from all_colors import *
from pygame.constants import *
pg.init()

size = (1200, 720)
screen = pg.display.set_mode(size)
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)

speed = 5
move = {K_LEFT:(-speed,0),
        K_RIGHT:(speed,0),
        K_UP:(0,-speed),
        K_DOWN:(0,speed)}


player = pg.Rect(0, 0, 100, 40)
player.midleft = (0, size[1]// 2)

enemy = pg.Rect(0, 0,100, 40)
enemy.midleft = (size[0]-100, size[1]// 2)


FPS = 60
clock = pg.time.Clock()

running = True
while running:
    old_pos = player.topleft
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()
    for key in move:
        if keys[key]:
            v = move[key]
            player.move_ip(v)

    if player.colliderect(enemy):
        player.topleft = old_pos



    screen.fill(BACKGROUND)
    pg.draw.rect(screen, RED, player)
    pg.draw.rect(screen, GREEN, enemy)
    pg.display.flip()
    clock.tick(FPS)

pg.quit()