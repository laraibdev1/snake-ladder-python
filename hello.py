import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Define constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

WIDTH = 600
HEIGHT = 400
SNAKE_SIZE = 10
SNAKE_SPEED = 15

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Hunting Apple Game")

# Clock to control the game speed
clock = pygame.time.Clock()

# Font for displaying the score
font_style = pygame.font.SysFont("bahnschrift", 25)

# Function to display the score
def Your_score(score):
    value = font_style.render("Your Score: " + str(score), True, WHITE)
    screen.blit(value, [0, 0])

# Function to draw the snake
def draw_snake(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_size, snake_size])

# Function to display the message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])

# Main function for the game
def gameLoop():
    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Random position for the apple
    foodx = round(random.randrange(0, WIDTH - SNAKE_SIZE) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - SNAKE_SIZE) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill(BLUE)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Event handling for movement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -SNAKE_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = SNAKE_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -SNAKE_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = SNAKE_SIZE
                    x1_change = 0

        # Check for boundary collision
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(BLUE)

        # Draw apple
        pygame.draw.rect(screen, RED, [foodx, foody, SNAKE_SIZE, SNAKE_SIZE])

        # Update snake position
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(SNAKE_SIZE, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        # Check if the snake eats the apple
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - SNAKE_SIZE) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - SNAKE_SIZE) / 10.0) * 10.0
            Length_of_snake += 1

        # Set the speed of the snake
        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

# Run the game
gameLoop()
