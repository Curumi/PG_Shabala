import pygame
from all_colors import *
import random
pygame.init()

# pygame.mixer.init()
# pygame.mixer.music.load('resources/la la land.mp3')
# pygame.mixer.music.play(-1)

size = (0,0)
screen = pygame.display.set_mode(size,pygame.FULLSCREEN)
pygame.display.set_caption("новая игра")
BACKGROUND = (255,255,255)
screen.fill(BACKGROUND)
# FPS = 1
clock = pygame.time.Clock()

COLORS = [BLACK,WHITE,RED,GREEN,YELLOW,CYAN,MAGENTA,GRAY,
          ORANGE,PINK,BROWN,PURPLE,LIME,NAVY,OLIVE,MAROON,TEAL,COLD]

running = True
timer = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(random.choice(COLORS))
    pygame.display.flip()
    pygame.time.delay(random.randint(200,200))
    # clock.tick(FPS)

pygame.quit()