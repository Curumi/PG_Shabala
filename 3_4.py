import pygame
import pygame.mixer
pygame.init()

pygame.mixer.init()

pygame.mixer.music.load('resours/Mge.mp3')

pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

shot_sound = pygame.mixer.Sound('resours/Mge.mp3')
explosion_sound = pygame.mixer.Sound('resours/Mge.mp3')
fail_sound = pygame.mixer.Sound('resours/Mge.mp3')
win_sound = pygame.mixer.Sound('resours/Mge.mp3')

shot_sound.set_volume(0.6)
win_sound.set_volume(0.2)

size = (1200, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("новая игра")
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)


volume = 5
FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                shot_sound.play(0)
            elif event.key == pygame.K_d:
                explosion_sound.play(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                volume += 0.1
                volume = min(volume, 1)
                shot_sound.set_volume(volume)
                explosion_sound.set_volume(volume)
                fail_sound.set_volume(volume)
                win_sound.set_volume(volume)
            if event.key == pygame.K_DOWN:
                volume -= 0.1
                volume = max(volume, 0)
                shot_sound.set_volume(volume)
                explosion_sound.set_volume(volume)
                fail_sound.set_volume(volume)
                win_sound.set_volume(volume)

    screen.fill(BACKGROUND)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
