import sys

import pygame as pg
from all_colors import *
from pygame.constants import *
pg.init()

# bounce_snd = pg.mixer.sound('resours/bounce.mp3')
# fail_snd = pg.mixer.sound('resours/fail.mp3')



SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BACKGROUND = (255, 255, 255)
screen.fill(BLACK)

PADDLE_WIDTH = 25
PADDLE_HEIGHT = 100
PADDLE_SPEED = 10

BALL_SIZE = 10
BALL_SPEED_X = 5
BALL_SPEED_y = 5


paddle1_rect = pg.Rect(0, SCREEN_HEIGHT//2 - PADDLE_HEIGHT//2,
                       PADDLE_WIDTH, PADDLE_HEIGHT)

paddle2_rect = pg.Rect(SCREEN_WIDTH - PADDLE_WIDTH,
                       SCREEN_HEIGHT//2 - PADDLE_HEIGHT//2,
                       PADDLE_WIDTH, PADDLE_HEIGHT)

ball_rect = pg.Rect(SCREEN_WIDTH//2 - BALL_SIZE//2,
                    SCREEN_HEIGHT//2 - BALL_SIZE//2,
                    BALL_SIZE, BALL_SIZE)

score1 = 0
score2 = 0

font = pg.font.Font(None, 32)

FPS = 60
clock = pg.time.Clock()
running = True


ai_mode = True

if len(sys.argv)>1:
    if sys.argv[1] == '--human':
        ai_mode = False

def score():
    pass
#if



def update_ai():
    if ball_rect.x > SCREEN_HEIGHT//2:
        if ball_rect.centery < paddle2_rect.centery:
            paddle2_rect.y -= PADDLE_SPEED
        elif ball_rect.centery > paddle2_rect.centery:
            paddle2_rect.y += PADDLE_SPEED

        if paddle2_rect.top < 0:
            paddle2_rect.top =0
        if paddle2_rect.bottom > SCREEN_HEIGHT:
            paddle2_rect.bottom = SCREEN_HEIGHT
    else:
        paddle2_rect.centery += (SCREEN_HEIGHT//2 - paddle2_rect.centery)/ PADDLE_SPEED

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()

    if keys[pg.K_w]:
        paddle1_rect.y -= PADDLE_SPEED
        if paddle1_rect.top <= 0:
            paddle1_rect.top = 0

    if keys[pg.K_s]:
        paddle1_rect.y += PADDLE_SPEED
        if paddle1_rect.bottom >= 720:
            paddle1_rect.bottom = 720

    if keys[pg.K_UP]:
        paddle2_rect.y -= PADDLE_SPEED
        if paddle2_rect.top <= 0:
            paddle2_rect.top = 0

    if keys[pg.K_DOWN]:
        paddle2_rect.y += PADDLE_SPEED
        if paddle2_rect.bottom >= 720:
            paddle2_rect.bottom = 720

    if ai_mode:
        update_ai()

    ball_rect.x += BALL_SPEED_X
    ball_rect.y += BALL_SPEED_y

    if ball_rect.top <=0 or ball_rect.bottom >= SCREEN_HEIGHT:
        BALL_SPEED_y *= -1


# Если поверхность мяча столкнулась с поверхностью 1 ракетки или поверхность мяча столкнулась с поверхностью второй ракетки - скорость мяча по оси икс умножить на -1

    if ball_rect.colliderect(paddle1_rect) or ball_rect.colliderect(paddle2_rect):
        BALL_SPEED_X *= -1

    if ball_rect.left <= 0:
        ball_rect = pg.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2,
                            SCREEN_HEIGHT // 2 - BALL_SIZE // 2,
                            BALL_SIZE, BALL_SIZE)

    if ball_rect.right >= 1200:
        ball_rect = pg.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2,
                            SCREEN_HEIGHT // 2 - BALL_SIZE // 2,
                            BALL_SIZE, BALL_SIZE)




    screen.fill(BLACK)

    pg.draw.rect(screen,WHITE, paddle1_rect)
    pg.draw.rect(screen, WHITE, paddle2_rect)
    pg.draw.ellipse(screen, WHITE, ball_rect)
    pg.draw.line(screen, WHITE,(SCREEN_WIDTH//2, 0), (SCREEN_WIDTH//2, SCREEN_HEIGHT))
    score_text = font.render(f'{score1} : {score2}', True, WHITE)
    screen.blit(score_text, (SCREEN_WIDTH//2 - score_text.get_width()//2, 10))
    pg.display.flip()
    clock.tick(FPS)

pg.quit()

#звуки увеличение скорости после удара (максимум 30) еще табло скорость и игру завершать