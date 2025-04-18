import pygame as pg
pg.init()

size = (1280, 720)
screen = pg.display.set_mode(size)
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)
FPS = 60
clock = pg.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            print(f"Press {event.key}")
        if event.type == pg.KEYUP:
            print(f"Release {event.key}")

    screen.fill(BACKGROUND)
    pg.display.flip()
    clock.tick(FPS)

pg.quit()