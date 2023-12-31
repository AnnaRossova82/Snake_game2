import pygame
import random
import time

speed_of_snake = 5

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

white_color = pygame.Color(255, 255, 255)
black_color = pygame.Color(0, 0, 0)
red_color = pygame.Color(250, 0, 0)
green_color = pygame.Color(124, 252, 0)

pygame.init()

display_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bg = pygame.transform.scale(pygame.image.load('font.jpg'), (SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('PYTHON - SNAKE')

game_clock = pygame.time.Clock()

position_of_snake = [450, 500]

body_of_snake = [
    [450, 500],
    [440, 500],
    [430, 500],
    [420, 500]
]

position_of_fruit = [
    random.randrange(1, (SCREEN_WIDTH//10)) * 10,
    random.randrange(1, (SCREEN_HEIGHT//10)) * 10
]
spawning_of_fruit = True

position_of_fruit_2 = [
    random.randrange(1, (SCREEN_WIDTH//10)) * 10,
    random.randrange(1, (SCREEN_HEIGHT//10)) * 10
]
spawning_of_fruit_2 = True


initial_direction = 'LEFT'
snake_direction = initial_direction

game_run = True

while game_run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                snake_direction = 'DOWN'
            if event.key == pygame.K_UP:
                snake_direction = 'UP'
            if event.key == pygame.K_LEFT:
                snake_direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                snake_direction = 'RIGHT'
            if event.key == pygame.K_w:
                snake_direction = 'UP'
            if event.key == pygame.K_a:
                snake_direction = 'LEFT'
            if event.key == pygame.K_s:
                snake_direction = 'DOWN'
            if event.key == pygame.K_d:
                snake_direction = 'RIGHT'

    if snake_direction == 'UP' and initial_direction != 'DOWN':
        initial_direction = 'UP'
    if snake_direction == 'DOWN' and initial_direction != 'UP':
        initial_direction = 'DOWN'
    if snake_direction == 'LEFT' and initial_direction != 'RIGHT':
        initial_direction = 'LEFT'
    if snake_direction == 'RIGHT' and initial_direction != 'LEFT':
        initial_direction = 'RIGHT'

    if snake_direction == 'W' and initial_direction != 'DOWN':
        initial_direction = 'UP'
    if snake_direction == 'S' and initial_direction != 'UP':
        initial_direction = 'DOWN'
    if snake_direction == 'A' and initial_direction != 'RIGHT':
        initial_direction = 'LEFT'
    if snake_direction == 'D' and initial_direction != 'LEFT':
        initial_direction = 'RIGHT'

    
    display_screen.fill(white_color)
    display_screen.blit(bg, (0, 0))

    if initial_direction == 'UP':
        position_of_snake[1] -= 10
    if initial_direction == 'DOWN':
        position_of_snake[1] += 10
    if initial_direction == 'LEFT':
        position_of_snake[0] -= 10
    if initial_direction == 'RIGHT':
        position_of_snake[0] += 10
    
    body_of_snake.insert(0, list(position_of_snake))
    if position_of_snake[0] == position_of_fruit[0] and position_of_snake[1] == position_of_fruit[1]:
        spawning_of_fruit = False
    elif position_of_snake[0] == position_of_fruit_2[0] and position_of_snake[1] == position_of_fruit_2[1]:
        spawning_of_fruit_2 = False
    else:
        body_of_snake.pop()

    if not spawning_of_fruit:
        position_of_fruit = [
            random.randrange(1, (SCREEN_WIDTH // 10)) * 10,
            random.randrange(1, (SCREEN_HEIGHT // 10)) * 10
        ]
    spawning_of_fruit = True
    
    if not spawning_of_fruit_2:
        position_of_fruit_2 = [
            random.randrange(1, (SCREEN_WIDTH // 10)) * 10,
            random.randrange(1, (SCREEN_HEIGHT // 10)) * 10
        ]

    spawning_of_fruit_2 = True


    for position in body_of_snake:
        pygame.draw.rect(display_screen, red_color, pygame.Rect(position[0], position[1], 10, 10))
        pygame.draw.rect(display_screen, red_color, pygame.Rect(position_of_fruit[0], position_of_fruit[1], 10, 10))
        pygame.draw.rect(display_screen, black_color, pygame.Rect(position_of_fruit_2[0], position_of_fruit_2[1], 10, 10))

  
    pygame.display.update()

    game_clock.tick(speed_of_snake)

pygame.quit()

