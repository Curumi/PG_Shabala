import pygame as pg
pg.init()

size = (1280, 720)
screen = pg.display.set_mode(size)
BACKGROUND = (0,0,0)
screen.fill(BACKGROUND)

points = []
spisok = []

show_preview = True

LINE_COLOR = (255,255,255)
PREVIEW_COLOR = (192,192,192)
FPS = 60
RADIUS = 5
clock = pg.time.Clock()

def remove_point(mouse_pos):
    for point in points:
        if ((point[0] - mouse_pos[0])**2 + (point[1] - mouse_pos[1]) **2 <= RADIUS **2):
            points.remove(point)
            break

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                points.append(event.pos)

            if event.button == 3:
                remove_point(event.pos)


    screen.fill(BACKGROUND)

    for i in range(len(points)-1):
        start_point = points[i]
        end_point = points[i+1]
        pg.draw.line(screen, (255,255,255), start_point, end_point)

    if len(points)>1:
        last_point = points[-1]
        mouse_pos = pg.mouse.get_pos()
        pg.draw.aaline(screen, (192,192,192), last_point, mouse_pos)

    pg.display.flip()
    clock.tick(FPS)

pg.quit()