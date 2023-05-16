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
  