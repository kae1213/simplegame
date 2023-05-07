
import pygame
import random

# Initialize Pygame
#just a new comment-iadded
pygame.init()

# window frame for game containment
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Roblox from Wish")

# Set up a single player
player_1_width = 50
player_1_height = 50
# Used for actual game visuals on the screen
player_1_x = screen_width / 2 - player_1_width / 2
player_1_y = screen_height - player_1_height
player_1_speed = 5
player_1_color = (255, 255, 0)

# Used to set up the enemy to hit the player
enemy_1_width = 50
enemy_1_height = 50
enemy_1_x = random.randint(0, screen_width - enemy_1_width)
#enemy_1_y = random.randint(0, screen_width - enemy_1_width)
enemy_1_y = 0
enemy_1_speed = 3
enemy_1_color = (255, 0, 0)

# Score and Pause Buttons
score = 0
score_font = pygame.font.Font(None, 36)
pause_font = pygame.font.Font(None, 42)

# Set up the game loop
is_game_running = True
clock = pygame.time.Clock()

while is_game_running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#only event to handle is quit
            is_game_running = False
        # Pause Game
        # New Game
        # Lost Game

    # Controls for player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_1_x > 0:
        player_1_x -= player_1_speed
    if keys[pygame.K_RIGHT] and player_1_x < screen_width - player_1_width:
        player_1_x += player_1_speed

    # Moving the enemy
    enemy_1_y += enemy_1_speed

    # Check and validate a collision
    if (player_1_x < enemy_1_x + enemy_1_width and player_1_x + player_1_width > enemy_1_x
            and player_1_y < enemy_1_y + enemy_1_height and player_1_y + player_1_height > enemy_1_y):
        enemy_1_x = random.randint(0, screen_width - enemy_1_width)
        enemy_1_y = 0
        score += 1

    # Draw screen for game
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, player_1_color, (player_1_x, player_1_y, player_1_width, player_1_height))
    pygame.draw.rect(screen, enemy_1_color, (enemy_1_x, enemy_1_y, enemy_1_width, enemy_1_height))
    score_text = score_font.render("Score: " + str(score), True, (255, 255, 255))
    pause_text = pause_font.render("|| ", True, (100, 100, 100))
    screen.blit(score_text, (10, 10))
    screen.blit(pause_text, (765, 10))
    pygame.display.flip()

    # Frame of game 60hz
    clock.tick(60)

# System Clear
pygame.quit()
