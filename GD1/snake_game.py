import pygame
import time
import random
import sys

# Initialize pygame
pygame.init()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
obstacle_color = (128, 0, 128)  # Purple color for obstacles

# Set display dimensions
width, height = 800, 600

# Create display
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Set clock for controlling the speed
clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

# Set fonts
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)


# Update the our_snake function to draw the snake head in a different color
def our_snake(snake_block, snake_list):
    for i, x in enumerate(snake_list):
        # Draw head in red, body in black
        if i == len(snake_list) - 1:
            pygame.draw.rect(dis, red, [x[0], x[1], snake_block, snake_block])
        else:
            pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


# Insert new function to display score
def show_score(score):
    value = score_font.render("Your Score: " + str(score), True, red)
    dis.blit(value, [0, 0])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [width / 6, height / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Generate food coordinates
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close == True:
            dis.fill(blue)
            message("You lost! Press C-Play Again or Q-Quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Check for boundaries
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Check if snake collides with itself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        show_score(Length_of_snake - 1)

        pygame.display.update()

        # Check if snake ate food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()


# New functions to demonstrate CodeCombat keywords integration
def spawnXY(objectType, x, y):
    """Spawn an object (enemy, item, obstacle) at coordinates x, y."""
    if objectType == 'obstacle':
        return {'type': 'obstacle', 'x': x, 'y': y, 'w': snake_block, 'h': snake_block}
    elif objectType == 'item':
        return {'type': 'item', 'x': x, 'y': y, 'w': snake_block, 'h': snake_block}
    return None


def spawnPlayerXY(x, y):
    """Spawn the player (snake head) at coordinates x, y."""
    return [x, y]


def addCollectGoal(itemType, target):
    """Define a collection goal, e.g., collect target number of items."""
    return {'item': itemType, 'target': target}


gameLoop()
