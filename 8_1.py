import pygame as pg
pg.init()

size = (1280, 720)
screen = pg.display.set_mode(size)
BACKGROUND = (0,0,0)
screen.fill(BACKGROUND)

points = []

FPS = 60
clock = pg.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.MOUSEBUTTONDOWN:
            points.append(event.pos)

    screen.fill(BACKGROUND)

    for i in range(len(points)-1):
        start_point = points[i]
        end_point = points[i+1]
        pg.draw.line(screen, (255,255,255), start_point, end_point)

    pg.display.flip()
    clock.tick(FPS)

pg.quit()