import pygame
from pygame.locals import *
import random
import communication
import serial
import struct
import menu_selection

# Initialize pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders from Wish")

# Set up the clock
clock = pygame.time.Clock()

# Set up the single player
player_image = pygame.image.load("assets/player.png")
player_width = 64
player_height = 64
player_x_position = (screen_width - player_width) // 2
player_y_position = screen_height - player_height - 10
player_speed = 15

#Player Controls
left_button_press_spaceGame = False
right_button_press_spaceGame = False
attack_button_press_spaceGame = False

# Set up the enemies
enemy_image = pygame.image.load("assets/enemy.png")
enemy_width = 64
enemy_height = 64
enemy_speed = 1
enemy_list = []
for i in range(5):
    enemy_x = random.randint(0, screen_width - enemy_width)
    enemy_y = random.randint(-200, -enemy_height)
    enemy_list.append((enemy_x, enemy_y))

# Set up the bullets
bullet_image = pygame.image.load("assets/bullet.png")
bullet_width = 16
bullet_height = 32
bullet_speed = 10
bullet_list = []

# Pause Button
pause_font = pygame.font.Font(None, 42)

# Set up the game loop
is_game_running = False

### Set Up Connection to Arduino ###
#arduino1 = serial.Serial('COM3', 9600)