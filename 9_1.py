import pygame as pg
from all_colors import COLORS
pg.init()

size = (800, 600)
screen = pg.display.set_mode(size)
BACKGROUND = (255, 255, 255)
background_color = (255, 255, 255)
brush_color = (0,0,0)
brush_width = 5

BORDER_COLOR = (0,0,0)
CUR_INDEX = 0

canvas = pg.Surface(screen.get_size())
canvas.fill(background_color)

size = 50
palette_rect = pg.Rect(10,10, size * 18, size)
palette = pg.Surface(palette_rect.size)
palette.fill(BACKGROUND)

def draw_palette():
    palette.fill(BACKGROUND)
    for i in range(18):
        color_rect = pg.Rect(i * size, 0, size, size)
        pg.draw.rect(palette, COLORS[i], color_rect)

    bonder_rect = pg.Rect(CUR_INDEX * size, 0, size, size)
    pg.draw.rect(palette, BORDER_COLOR, bonder_rect, width = 3)
    screen.blit(palette, palette_rect.topleft)



screen.fill(BACKGROUND)


dragging_palett  = False

FPS = 60
clock = pg.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
            print('рыпаемся')
            dragging_palett = True
            offset = (event.pos[0] - palette_rect.left, event.pos[1] - palette_rect.top)

        elif event.type == pg.MOUSEBUTTONUP and event.button == 3:
            print('сидим, не рыпаемся')
            dragging_palett = False

    if dragging_palett:
        new_pos = (mouse_pos[0] - offset[0], mouse_pos[1] - offset[1])
        palette_rect.topleft = new_pos



    mouse_pos = pg.mouse.get_pos()
    mouse_pressed = pg.mouse.get_pressed()

    if mouse_pressed[0]:
        if palette_rect.collidepoint(mouse_pos):
            print(mouse_pos)
            if palette_rect.collidepoint(mouse_pos):
                selected_color_index = ((mouse_pos[0] - palette_rect.left) // size)
                CUR_INDEX = selected_color_index
                brush_color = COLORS[CUR_INDEX]
        else:
            pg.draw.circle(canvas, brush_color, mouse_pos, brush_width)


    screen.blit(canvas, (0, 0))
    draw_palette()
    pg.display.flip()
    clock.tick(FPS)

pg.quit()