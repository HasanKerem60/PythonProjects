# Nokia Snake Game

import pygame
import random
import sys

# Başlat
pygame.init()

# Renkler
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Ekran boyutu (resme göre)
WINDOW_WIDTH = 980
WINDOW_HEIGHT = 980

# Oyun alanı: dikdörtgen ve küçültülmüş
SCREEN_TOPLEFT = (358, 153)
SCREEN_WIDTH = 263
SCREEN_HEIGHT = 342

# Kare boyutu
BLOCK_SIZE = 15

# Pencere oluştur
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Nokia Snake on Phone")
clock = pygame.time.Clock()

# Arka plan resmi
bg = pygame.image.load("nokia.png")
bg = pygame.transform.scale(bg, (WINDOW_WIDTH, WINDOW_HEIGHT))

# Yılan başlangıcı
snake = [(SCREEN_TOPLEFT[0] + 45, SCREEN_TOPLEFT[1] + 45)]
snake_dir = (BLOCK_SIZE, 0)

# Yem
food = (SCREEN_TOPLEFT[0] + 75, SCREEN_TOPLEFT[1] + 75)

# Puan
score = 0
font = pygame.font.SysFont("Courier", 20)

def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, BLACK, pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

def draw_food():
    pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))

def show_score():
    text = font.render("Puan: " + str(score), True, WHITE)
    screen.blit(text, (10, 10))

def get_random_food():
    x = random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE + SCREEN_TOPLEFT[0]
    y = random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE + SCREEN_TOPLEFT[1]
    return (x, y)

# Ana döngü
running = True
while running:
    screen.fill(BLACK)
    screen.blit(bg, (0, 0))
    pygame.draw.rect(screen, GREEN, (SCREEN_TOPLEFT[0], SCREEN_TOPLEFT[1], SCREEN_WIDTH, SCREEN_HEIGHT))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, BLOCK_SIZE):
                snake_dir = (0, -BLOCK_SIZE)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -BLOCK_SIZE):
                snake_dir = (0, BLOCK_SIZE)
            elif event.key == pygame.K_LEFT and snake_dir != (BLOCK_SIZE, 0):
                snake_dir = (-BLOCK_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-BLOCK_SIZE, 0):
                snake_dir = (BLOCK_SIZE, 0)

    # Hareket
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    snake.insert(0, new_head)

    # Yem yeme
    if snake[0] == food:
        score += 10
        food = get_random_food()
    else:
        snake.pop()

    # Çarpma kontrolü
    x, y = snake[0]
    if (x < SCREEN_TOPLEFT[0] or x >= SCREEN_TOPLEFT[0] + SCREEN_WIDTH or
        y < SCREEN_TOPLEFT[1] or y >= SCREEN_TOPLEFT[1] + SCREEN_HEIGHT or
        snake[0] in snake[1:]):
        snake = [(SCREEN_TOPLEFT[0] + 45, SCREEN_TOPLEFT[1] + 45)]
        snake_dir = (BLOCK_SIZE, 0)
        score = 0
        food = get_random_food()

    # Çizim
    draw_food()
    draw_snake()
    show_score()

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
sys.exit()
