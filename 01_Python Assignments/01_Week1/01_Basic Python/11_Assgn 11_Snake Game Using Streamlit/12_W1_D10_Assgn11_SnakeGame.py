import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
green = (0, 200, 0)
red = (200, 0, 0)
black = (0, 0, 0)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, green, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

def show_score(score):
    value = font.render(f"Score: {score}", True, black)
    screen.blit(value, [10, 10])

def game_loop():
    game_over = False
    game_close = False

    x = WIDTH // 2
    y = HEIGHT // 2
    x_change = 0
    y_change = 0

    snake = []
    snake_length = 1

    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20

    while not game_over:

        while game_close:
            screen.fill(white)
            msg = font.render("Game Over! Press Q-Quit or C-Play Again", True, red)
            screen.blit(msg, [50, HEIGHT // 2])
            show_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -BLOCK_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = BLOCK_SIZE
                    x_change = 0

        x += x_change
        y += y_change

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        screen.fill(white)
        pygame.draw.rect(screen, red, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        snake_head = [x, y]
        snake.append(snake_head)

        if len(snake) > snake_length:
            del snake[0]

        for block in snake[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake)
        show_score(snake_length - 1)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20
            snake_length += 1

        clock.tick(10)

    pygame.quit()
    sys.exit()

game_loop()