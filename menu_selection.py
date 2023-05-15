import sys
import pygame
from pygame.locals import *

# Init Screen
pygame.init()

# window frame for menu containment
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

#Kelvin: New global vars
title_text_width = 0
title_text_height = 0
title_text_x_position = 0
title_text_y_position= 0

# function for menu selection
def display_menu(selected_option):

    # Clear the screen
    screen.fill((0, 0, 0))

    # Text for Main Title 
    font_title = pygame.font.Font(None, 48)
    title_text = "!Wish Presents!"
    title = font_title.render(title_text, True, (255, 255, 255))
    screen.blit(title, (screen_width/2 - title.get_width()/2, 50))

    title_text_width, title_text_height = font_title.size(title_text)
    title_text_x_position = (screen_width - title_text_width) // 2
    title_text_y_position = (screen_height - title_text_height) // 2

    # Menu Options
    font = pygame.font.Font(None, 36)

    text1 = font.render("Roblox from Wish", True, (255, 255, 255))
    text2 = font.render("Space Invaders from Wish", True, (255, 255, 255))
    text3 = font.render("Vortex", True, (255, 255, 255))
 
    screen.blit(text1, (screen_width/2 - text1.get_width()/2, screen_height/2 - text1.get_height()))
    screen.blit(text2, (screen_width/2 - text2.get_width()/2, screen_height/2))
    screen.blit(text3, (screen_width/2 - text3.get_width()/2, screen_height/2 + text3.get_height()))

    # Will highlight menu's selection
    if selected_option == 1:
        pygame.draw.rect(screen, (255, 0, 0), (screen_width/2 - text1.get_width()/2 - 10, screen_height/2 - text1.get_height() - 5, text1.get_width() + 20, text1.get_height() + 10), 2)
    elif selected_option == 2:
        pygame.draw.rect(screen, (255, 0, 0), (screen_width/2 - text2.get_width()/2 - 10, screen_height/2 - 5, text2.get_width() + 20, text2.get_height() + 10), 2)
    elif selected_option == 3:
        pygame.draw.rect(screen, (255, 0, 0), (screen_width/2 - text3.get_width()/2 - 10, screen_height/2 + text3.get_height() - 5, text3.get_width() + 20, text3.get_height() + 10), 2)

    # Draw contents for the game selection selection screen
    screen.blit(text1, (screen_width/2 - text1.get_width()/2, screen_height/2 - text1.get_height()))
    screen.blit(text2, (screen_width/2 - text2.get_width()/2, screen_height/2))
    screen.blit(text3, (screen_width/2 - text3.get_width()/2, screen_height/2 + text3.get_height()))

    pygame.display.flip()
# Functionality for choosing which game
def game1():
    selected_option = 1
    print('Selected opt 1')
    while True:
        # Game 1 logic
        #Kelvin: Uncomment for debugging puposes to halt
        #sys.exit() 
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    selected_option = 1
                elif event.key == K_DOWN:
                    selected_option = 2
                elif event.key == K_ESCAPE:
                    display_menu(selected_option)
                    print('Selected')
                    return

    display_menu(selected_option)
    #return
def game2():
    while True:
        print('Selected opt 2')
        sys.exit() 
        # Game 2 logic
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                display_menu()
                print('Selected')
                return
def game3():
    while True:
        print('Selected opt 3')
        sys.exit() 
        # Game 2 logic
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                display_menu()
                print('Selected')
                return
