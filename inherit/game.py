import pygame
from pygame.locals import *
import random
import communication
import serial
import struct
import menu_selection

# Initialize Pygame
pygame.init()

# window frame for game containment
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Roblox from Wish")

#Set Game Clock
clock = pygame.time.Clock()

# Set up a single player
player_1_width = 50
player_1_height = 50

#Player Controls
left_button_pressed_game1 = False
right_button_pressed_game1 = False
empty_var = False

# Used for game visuals on the screen
player_1_x_position = screen_width / 2 - player_1_width / 2
player_1_y_position = screen_height - player_1_height
player_1_speed = 15
player_1_color = (255, 255, 0)

# Used to set up the enemy to hit the player
enemy_1_width = 50
enemy_1_height = 50
enemy_1_x_position = random.randint(0, screen_width - enemy_1_width)
enemy_1_y_position = 0
enemy_1_speed = 3
enemy_1_color = (255, 0, 0)

# Score and Pause Buttons
score = 0
score_font = pygame.font.Font(None, 36)
pause_font = pygame.font.Font(None, 42)

# Set up the game loop
is_game_running = True

### Set Up Connection to Arduino ###
arduino1 = serial.Serial('COM3', 9600)

# Game logic to start
while is_game_running:
    # Handle events
    if arduino1.in_waiting > 0:
        # read data from serial connection
        data = arduino1.read().decode('utf-8')
        # handle incoming data here
        print('Received character: {}'.format(data))
        print('Received Type: ', type(data))
        left_button_pressed_game1, right_button_pressed_game1, empty_var  = communication.button_state(data)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:#only event to handle is quit
            is_game_running = False
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            if pause_rect.collidepoint(event.pos):
                print("Toggle Back")
                menu_selection.display_menu(2)

    # Controls for player movement
    #if keys[pygame.K_LEFT] and player_1_x_position > 0:
    if left_button_pressed_game1 and player_1_x_position > 0:
        player_1_x_position -= player_1_speed
        left_button_pressed_game1 = False
        
    #if keys[pygame.K_RIGHT] and player_1_x_position < screen_width - player_1_width:
    if right_button_pressed_game1 and player_1_x_position > 0:
        player_1_x_position += player_1_speed
        right_button_pressed_game1 = False

    # Moving the enemy
    enemy_1_y_position += enemy_1_speed

    # Check and validate a collision
    if (player_1_x_position < enemy_1_x_position + enemy_1_width and player_1_x_position + player_1_width > enemy_1_x_position
            and player_1_y_position < enemy_1_y_position + enemy_1_height and player_1_y_position + player_1_height > enemy_1_y_position):
        enemy_1_x_position = random.randint(0, screen_width - enemy_1_width)
        enemy_1_y_position = 0
        score += 1

    # Draw screen for game
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, player_1_color, (player_1_x_position, player_1_y_position, player_1_width, player_1_height))
    pygame.draw.rect(screen, enemy_1_color, (enemy_1_x_position, enemy_1_y_position, enemy_1_width, enemy_1_height))

    score_text = score_font.render("Score: " + str(score), True, (255, 255, 255))

    pause_text = pause_font.render("|| ", True, (100, 100, 100))
    pause_rect = pause_text.get_rect()
    pause_rect.topright = (screen_width - 10, 10)
    
    # Draw All Needed Text
    screen.blit(score_text, (10, 10))
    screen.blit(pause_text, pause_rect)
    
    #Update Screen
    pygame.display.flip()

    # Frame of game 60hz
    clock.tick(60)

# System and Controller Clear
#Kelvin: It looks like game execution without a problem, you probably wont need it
arduino1.close()
pygame.quit()