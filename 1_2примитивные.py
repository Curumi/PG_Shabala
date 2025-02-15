import pygame.draw

from all_colors import *
import pygame as pg
pg.init()

size = (1280, 720)
screen = pg.display.set_mode(size)
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)
line_color = RED
line_width = 5
start_pos = (0, size[1]//2)
end_pos = (size[0], size[1]//2)

FPS = 60
clock = pg.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill(BACKGROUND)

    pygame.draw.line(screen, line_color, start_pos, end_pos, line_width)

    pygame.draw.rect(screen,ORANGE, (50,50,100,100))

    pygame.draw.rect(screen,ORANGE, (250, 50, 100, 100),1)

    pygame.draw.rect(screen, ORANGE, (450, 50, 100, 100),border_radius = 10)

    pygame.draw.ellipse(screen, ORANGE, (50, 450, 100, 100))

    pygame.draw.ellipse(screen, ORANGE, (250, 450, 100, 100),1)

    pygame.draw.polygon(screen, ORANGE, ((750, 250),(800, 300),(850, 250)))













    pg.display.flip()
    clock.tick(FPS)

pg.quit()