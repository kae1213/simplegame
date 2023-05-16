import pygame
from pygame.locals import *
import random

# Initialize Pygame
pygame.init()

# window frame for game containment
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game 3")

#Set Game Clock
clock = pygame.time.Clock()

# Set Up Pause Font
pause_font = pygame.font.Font(None, 42)

# Set up the game loop
is_game_running = True

# arduino data to send 
startGame = 'B'
endGame = '4'


