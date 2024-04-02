import pygame
import random

# Initialize Pygame
pygame.init()

# Set up screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
# Set up colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up snake and food properties
BLOCK_SIZE = 20
SNAKE_SPEED = 10

# Set up font
font = pygame.font.SysFont(None, 25)

# Function to draw the snake
def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

# Function to generate food
def generate_food(snake_list):
    while True:
        food_x = random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
        food_y = random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
        if [food_x, food_y] not in snake_list:
            return food_x, food_y

# Function to display score and level
def display_info(score, level):
    score_text = font.render("Score: " + str(score), True, WHITE)
    level_text = font.render("Level: " + str(level), True, WHITE)
    screen.blit(score_text, [10, 10])
    screen.blit(level_text, [SCREEN_WIDTH - 100, 10])

# Function to display game over message
def game_over():
    message = font.render("Game Over! Press Q to Quit or R to Restart", True, WHITE)
    screen.blit(message, [SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2])

# Main function
def main():
    # Set up screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")

    # Initialize variables
    snake_list = [[100, 50], [90, 50], [80, 50]]
    snake_length = 3
    direction = 'RIGHT'
    food_x, food_y = generate_food(snake_list)
    score = 0
    level = 1
    clock = pygame.time.Clock()

    # Game loop
    game_over_flag = False
    while not game_over_flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over_flag = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'
                elif event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'
                elif event.key == pygame.K_q:
                    game_over_flag = True
                elif event.key == pygame.K_r:
                    main()

        # Move the snake
        if direction == 'RIGHT':
            snake_head = [snake_list[0][0] + BLOCK_SIZE, snake_list[0][1]]
        elif direction == 'LEFT':
            snake_head = [snake_list[0][0] - BLOCK_SIZE, snake_list[0][1]]
        elif direction == 'UP':
            snake_head = [snake_list[0][0], snake_list[0][1] - BLOCK_SIZE]
        elif direction == 'DOWN':
            snake_head = [snake_list[0][0], snake_list[0][1] + BLOCK_SIZE]

        # Check for wall collision
        if (snake_head[0] < 0 or snake_head[0] >= SCREEN_WIDTH or
            snake_head[1] < 0 or snake_head[1] >= SCREEN_HEIGHT):
            game_over_flag = True

        # Check for snake collision
        if snake_head in snake_list[1:]:
            game_over_flag = True

        snake_list.insert(0, snake_head)
        if snake_head[0] == food_x and snake_head[1] == food_y:
            score += 10
            snake_length += 1
            food_x, food_y = generate_food(snake_list)
            if score % 30 == 0:  # Increase level every 3 foods
                level += 1

        else:
            snake_list.pop()

        # Draw everything
        screen.fill(0)
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        draw_snake(snake_list)
        display_info(score, level)
        pygame.display.update()

        # Set game speed
        clock.tick(SNAKE_SPEED + (level - 1) * 2)

    # Game over
    game_over()
    pygame.display.update()
    pygame.quit()
    quit()

# Start the game
if __name__ == "__main__":
    main()