def get_closest_point(mouse_pos):
    closest_point = None
    closest_distance = float('inf')
    for point in points:
        distance = ((point[0] - mouse_pos[0])**2 +
                    (point[1] - mouse_pos[1])**2)**0.5

        if distance <= RADIUS**2 and distance < closest_distance:
            closest_point = point
            closest_distance = distance
    return  closest_point





def remove_point(mouse_pos):
    for point in points:
        if ((point[0] - mouse_pos[0])**2 + (point[1] - mouse_pos[1])**2
        <= RADIUS**2):
            points.remove(point)
            break



import pygame
pygame.init()




size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("новая игра")
BACKGROUND = (0,0,0)
screen.fill(BACKGROUND)
COLORS = (192,192,192)
LINE_COLOR = (255,255,255)

points = []
RADIUS = 5
RED = (255,0,0)


FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    closest_point = get_closest_point(mouse_pos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        elif event.type == pygame.MOUSEBUTTONDOWN:
            if closest_point:

                if event.button == 1:
                    points.append(closest_point)

                elif event.button == 3:
                    remove_point(closest_point)

            elif event.button == 1:
                points.append(mouse_pos)


    screen.fill(BACKGROUND)

    for i in range(len(points)-1):
        pygame.draw.line(screen,LINE_COLOR,points[i],points[i+1],3)

    if len(points)>1:
        pygame.draw.aaline(screen, COLORS,points[-1],mouse_pos, 3)

    if closest_point:
        pygame.draw.circle(screen,RED,closest_point,RADIUS,1)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()