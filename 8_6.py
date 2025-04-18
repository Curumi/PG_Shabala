# Левая кнопка + режим рисования
# Правая кнопка – переключить режим



import pygame
pygame.init()
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Рисование линий")
BACKGROUND = (0, 0, 0)
screen.fill(BACKGROUND)

LINE_COLOR = (255, 255, 255)
PREVIEW_COLOR = (192, 192, 192)

figures = [[]]
drawing_mode = True

FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and drawing_mode:
                figures[-1].append(event.pos)
            elif event.button == 3:
                drawing_mode = not drawing_mode
                if drawing_mode:
                    figures.append([])


    screen.fill(BACKGROUND)


    for figure in figures:
        for i in range(len(figure) - 1):
            start_point = figure[i]
            end_point = figure[i + 1]
            pygame.draw.line(screen, LINE_COLOR, start_point, end_point, 3)


    if len(figures[-1]) > 0 and drawing_mode:
        last_point = figures[-1][-1]
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.aaline(screen, PREVIEW_COLOR, last_point, mouse_pos, 3)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()