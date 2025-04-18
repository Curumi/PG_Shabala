import math
import random
import pygame as pg

pg.init()

# Загрузка изображений
pacman_images = {
    'up': pg.image.load('resours/pacman_up.png'),
    'down': pg.image.load('resours/pacman_down.png'),
    'left': pg.image.load('resours/pacman_left.png'),
    'right': pg.image.load('resours/pacman_right.png'),
    'up_left': pg.image.load('resours/pacman_up_left.png'),
    'up_right': pg.image.load('resours/pacman_up_right.png'),
    'down_left': pg.image.load('resours/pacman_down_left.png'),
    'down_right': pg.image.load('resours/pacman_down_right.png')
}

# Константы
SIZE = (640, 480)
BACKGROUND = (0, 0, 0)
CIRCLE_COLOR = (255, 255, 255)
CIRCLE_RADIUS = 10
FPS = 60
PACMAN_SPEED = 3
GHOST_SPEED = 2
PELLET_COLOR = (255, 255, 0)
PELLET_RADIUS = 3


def get_direction(pos1, pos2):
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]

    if abs(dx) > abs(dy):
        return 'right' if dx > 0 else 'left'
    else:
        return 'down' if dy > 0 else 'up'


def distance(pos1, pos2):
    return math.sqrt((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2)


def move_towards(pos1, pos2, speed):
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]
    dist = distance(pos1, pos2)

    if dist == 0:
        return pos1

    dx = dx / dist * speed
    dy = dy / dist * speed

    return (pos1[0] + dx, pos1[1] + dy)


class Ghost:
    def __init__(self, x, y):
        self.pos = [x, y]
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))

    def move(self, target_pos):
        self.pos = move_towards(self.pos, target_pos, GHOST_SPEED)

    def draw(self, screen):
        pg.draw.circle(screen, self.color, (int(self.pos[0]), int(self.pos[1])), CIRCLE_RADIUS)


class Pellet:
    def __init__(self, x, y):
        self.pos = (x, y)

    def draw(self, screen):
        pg.draw.circle(screen, PELLET_COLOR, self.pos, PELLET_RADIUS)


# Инициализация игры
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Pac-Man")
clock = pg.time.Clock()

pacman_pos = [SIZE[0] // 2, SIZE[1] // 2]
ghosts = [Ghost(random.randint(0, SIZE[0]), random.randint(0, SIZE[1])) for _ in range(4)]
pellets = [Pellet(random.randint(0, SIZE[0]), random.randint(0, SIZE[1])) for _ in range(50)]

score = 0
font = pg.font.Font(None, 36)

# Центрирование мыши
pg.mouse.set_pos(SIZE[0] // 2, SIZE[1] // 2)
pg.event.set_grab(True)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False

    # Обновление позиции Pac-Man
    mouse_pos = pg.mouse.get_pos()
    direction = get_direction(pacman_pos, mouse_pos)
    pacman_pos = move_towards(pacman_pos, mouse_pos, PACMAN_SPEED)

    # Обновление призраков
    for ghost in ghosts:
        ghost.move(pacman_pos)

    # Проверка столкновений с пеллетами
    for pellet in pellets[:]:
        if distance(pacman_pos, pellet.pos) < CIRCLE_RADIUS + PELLET_RADIUS:
            pellets.remove(pellet)
            score += 10

    # Проверка столкновений с призраками
    for ghost in ghosts:
        if distance(pacman_pos, ghost.pos) < CIRCLE_RADIUS * 2:
            running = False

    # Отрисовка
    screen.fill(BACKGROUND)

    for pellet in pellets:
        pellet.draw(screen)

    for ghost in ghosts:
        ghost.draw(screen)

    pacman_image = pacman_images[direction]
    screen.blit(pacman_image, (int(pacman_pos[0] - CIRCLE_RADIUS), int(pacman_pos[1] - CIRCLE_RADIUS)))

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pg.display.flip()
    clock.tick(FPS)

pg.quit()