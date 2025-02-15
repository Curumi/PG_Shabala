import pygame
from all_colors import *
import random
pygame.init()

pygame.mixer.init()
pygame.mixer.music.load('resours/Mge.mp3')
pygame.mixer.music.play(-1)

size = (0, 0)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.display.set_caption("новая игра")
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)
# FPS = 1
clock = pygame.time.Clock()

COLORS = [BLACK, WHITE, RED, GREEN, YELLOW, CYAN, MAGENTA, GRAY,
          ORANGE, PINK, BROWN, PURPLE, LIME, NAVY, OLIVE, MAROON, TEAL, GOLD]

running = True
timer = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(random.choice(COLORS))
    pygame.time.delay(random.randint(200, 200))

    for _ in range(10):
        x = random.randint(0, 1000)
        y = random.randint(0, 1000)
        radius = random.randint(10, 100)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.circle(screen, color, (x, y), radius)

        pygame.display.flip()

pygame.quit()