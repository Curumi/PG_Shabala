import math
import pygame
import random
import time

pygame.init()

# Загрузка изображений
pacman_images = {
    'up': pygame.image.load('resours/pacman_up.png'),
    'down': pygame.image.load('resours/pacman_down.png'),
    'left': pygame.image.load('resours/pacman_left.png'),
    'right': pygame.image.load('resours/pacman_right.png'),
    'up_left': pygame.image.load('resours/pacman_up_left.png'),
    'up_right': pygame.image.load('resours/pacman_up_right.png'),
    'down_left': pygame.image.load('resours/pacman_down_left.png'),
    'down_right': pygame.image.load('resours/pacman_down_right.png'),
}

class Dot:
    def __init__(self, pos):
        self.pos = pos
        self.collected = False
        self.radius = 5
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self, screen):
        if not self.collected:
            pygame.draw.circle(screen, self.color, self.pos, self.radius)

def create_dots(count, size):
    dots = []
    for _ in range(count):
        x = random.randint(50, size[0] - 50)
        y = random.randint(50, size[1] - 50)
        dots.append(Dot((x, y)))
    return dots

def get_direction(pos1, pos2):
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]

    direction = 'right'

    if dy < 0:
        if dx < 0:
            direction = 'up_left'
        elif dx > 0:
            direction = 'up_right'
        else:
            direction = 'up'
    elif dy > 0:
        if dx < 0:
            direction = 'down_left'
        elif dx > 0:
            direction = 'down_right'
        else:
            direction = 'down'
    else:
        if dx < 0:
            direction = 'left'
        elif dx > 0:
            direction = 'right'

    return direction

def distance(pos1, pos2):
    return math.sqrt((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2)

def move_towards(pos1, pos2, min_speed=1, max_speed=3):
    x1, y1 = pos1
    x2, y2 = pos2
    dx = x2 - x1
    dy = y2 - y1

    dist = distance(pos1, pos2)

    if dist < min_speed:
        return pos2

    if dist == 0:
        return pos1

    speed = max(min_speed, min(dist / 5, max_speed))

    dx /= dist
    dy /= dist

    x1 += dx * speed
    y1 += dy * speed

    return (x1, y1)

def show_roulette(screen, size, player_score):
    # Цвета для рулетки
    roulette_colors = [
        (255, 0, 0), (0, 0, 0), (255, 0, 0), (0, 0, 0), (255, 0, 0), (0, 0, 0),
        (255, 0, 0), (0, 0, 0), (255, 0, 0), (0, 0, 0), (255, 0, 0), (0, 0, 0),
        (255, 0, 0), (0, 0, 0), (255, 0, 0), (0, 0, 0), (255, 0, 0), (0, 0, 0),
        (255, 0, 0), (0, 0, 0), (255, 0, 0), (0, 0, 0), (255, 0, 0), (0, 0, 0),
        (255, 0, 0), (0, 0, 0), (255, 0, 0), (0, 0, 0), (255, 0, 0), (0, 0, 0),
        (255, 0, 0), (0, 0, 0), (255, 0, 0), (0, 0, 0), (255, 0, 0), (0, 0, 0)
    ]
    
    # Числа на рулетке
    roulette_numbers = [
        0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10,
        5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26
    ]
    
    # Параметры рулетки
    wheel_radius = min(size) // 3
    wheel_center = (size[0] // 2, size[1] // 2)
    segments = len(roulette_numbers)
    segment_angle = 360 / segments
    
    # Анимация вращения
    spinning = True
    spin_speed = 25
    spin_duration = 100  # Количество кадров анимации
    spin_frame = 0
    winning_number = None
    
    # Текст
    font_large = pygame.font.SysFont(None, 72)
    font_small = pygame.font.SysFont(None, 36)
    
    clock = pygame.time.Clock()
    
    while spinning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return player_score
        
        # Очистка экрана
        screen.fill((0, 100, 0))  # Зеленый фон как в казино
        
        # Отрисовка рулетки
        current_angle = spin_frame * spin_speed % 360
        
        for i in range(segments):
            angle = i * segment_angle + current_angle
            start_angle = math.radians(angle)
            end_angle = math.radians(angle + segment_angle)
            
            # Отрисовка сегмента
            pygame.draw.arc(screen, roulette_colors[i % len(roulette_colors)], 
                            (wheel_center[0] - wheel_radius, wheel_center[1] - wheel_radius, 
                             wheel_radius * 2, wheel_radius * 2),
                            start_angle, end_angle, wheel_radius)
            
            # Отрисовка числа
            text = font_small.render(str(roulette_numbers[i]), True, (255, 255, 255))
            text_angle = angle + segment_angle / 2
            text_pos = (
                wheel_center[0] + math.cos(math.radians(text_angle)) * wheel_radius * 0.7 - text.get_width() / 2,
                wheel_center[1] + math.sin(math.radians(text_angle)) * wheel_radius * 0.7 - text.get_height() / 2
            )
            screen.blit(text, text_pos)
        
        # Отрисовка указателя
        pygame.draw.polygon(screen, (255, 215, 0), [
            (wheel_center[0], wheel_center[1] - wheel_radius - 20),
            (wheel_center[0] - 10, wheel_center[1] - wheel_radius),
            (wheel_center[0] + 10, wheel_center[1] - wheel_radius)
        ])
        
        # Отображение текста
        title_text = font_large.render("Roulette Time!", True, (255, 255, 255))
        screen.blit(title_text, (size[0] // 2 - title_text.get_width() // 2, 50))
        
        # Завершение анимации
        spin_frame += 1
        if spin_frame >= spin_duration:
            spinning = False
            winning_index = int(current_angle / segment_angle) % segments
            winning_number = roulette_numbers[winning_index]
            
            # Определение выигрыша
            if winning_number == 0:
                win_multiplier = 35
            elif winning_number % 2 == 0:
                win_multiplier = 2  # Четные числа
            else:
                win_multiplier = 2  # Нечетные числа
            
            # Красные числа дают дополнительный бонус
            if roulette_colors[winning_index % len(roulette_colors)] == (255, 0, 0):
                win_multiplier += 1
            
            player_score += win_multiplier * 5
        
        pygame.display.flip()
        clock.tick(30)
    
    # Показ результата
    result_text = font_large.render(f"Выпало: {winning_number}", True, (255, 255, 255))
    win_text = font_large.render(f"+{win_multiplier * 5} очков!", True, (255, 255, 0))
    
    screen.fill((0, 100, 0))
    screen.blit(result_text, (size[0] // 2 - result_text.get_width() // 2, size[1] // 2 - 50))
    screen.blit(win_text, (size[0] // 2 - win_text.get_width() // 2, size[1] // 2 + 50))
    pygame.display.flip()
    pygame.time.wait(3000)
    
    return player_score

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pac-Man Турнир")
BACKGROUND = (0, 0, 0)
FPS = 60
clock = pygame.time.Clock()

player_pos = [400, 300]
player_score = 0
dots = create_dots(50, size)
game_time = 180
start_time = time.time()

running = True
while running:
    current_time = time.time()
    elapsed = current_time - start_time
    remaining_time = max(0, game_time - elapsed)

    if remaining_time <= 0:
        running = False
        result = "Время вышло!"
        screen.fill(BACKGROUND)
        font = pygame.font.SysFont(None, 72)
        text = font.render(result, True, (255, 255, 255))
        screen.blit(text, (size[0] // 2 - text.get_width() // 2, size[1] // 2 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(3000)
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pos = pygame.mouse.get_pos()
    player_direction = get_direction(player_pos, mouse_pos)
    player_pos = list(move_towards(player_pos, mouse_pos))

    if all(dot.collected for dot in dots):
        dots = create_dots(50, size)

    player_rect = pygame.Rect(player_pos[0] - 15, player_pos[1] - 15, 30, 30)

    for dot in dots:
        if not dot.collected:
            dot_rect = pygame.Rect(dot.pos[0] - dot.radius, dot.pos[1] - dot.radius,
                                 dot.radius * 2, dot.radius * 2)

            if player_rect.colliderect(dot_rect):
                dot.collected = True
                player_score += 1

                if player_score == 10:
                    player_score = show_roulette(screen, size, player_score)

    screen.fill(BACKGROUND)

    for dot in dots:
        dot.draw(screen)

    screen.blit(pacman_images[player_direction], (player_pos[0] - 15, player_pos[1] - 15))

    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Игрок: {player_score}", True, (255, 255, 255))
    time_text = font.render(f"Время: {int(remaining_time // 60)}:{int(remaining_time % 60):02d}", True, (255, 255, 255))

    screen.blit(score_text, (20, 20))
    screen.blit(time_text, (size[0] - time_text.get_width() - 20, 20))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
