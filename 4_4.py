import pygame
pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Два самолета с изображениями")


background = pygame.image.load("resources/nedo.png")
player1_image = pygame.image.load("resources/plane1.png")
player2_image = pygame.image.load("resources/plane2.png")


background = pygame.transform.scale(background, (width, height))
player1_image = pygame.transform.scale(player1_image, (150, 150))
player2_image = pygame.transform.scale(player2_image, (150, 150))


player1_pos = [100, 300]
player2_pos = [700, 300]


running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1_pos[1] -= 5
    if keys[pygame.K_s]:
        player1_pos[1] += 5
    if keys[pygame.K_a]:
        player1_pos[0] -= 5
    if keys[pygame.K_d]:
        player1_pos[0] += 5

    player1_pos[0] = max(0, min(player1_pos[0], width - 150))
    player1_pos[1] = max(0, min(player1_pos[1], height - 150))

    mouse_pos = pygame.mouse.get_pos()
    player2_pos[0] = max(0, min(mouse_pos[0] - 75, width - 150))
    player2_pos[1] = max(0, min(mouse_pos[1] - 75, height - 150))

    screen.blit(background, (0, 0))
    screen.blit(player1_image, player1_pos)
    screen.blit(player2_image, player2_pos)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
