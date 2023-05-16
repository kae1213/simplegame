import game1Defines
import pygame
import menu_selection
from pygame.locals import *
import random
import serial

def initGame1():
    arduino1 = serial.Serial('COM3', 9600)
    while game1Defines.is_game_running:
    # Handle events
        if arduino1.in_waiting > 0:
            # read data from serial connection
            data = arduino1.read().decode('utf-8')
            # handle incoming data here
            print('Received character: {}'.format(data))
            print('Received Type: ', type(data))
            game1Defines.left_button_pressed_game1, game1Defines.right_button_pressed_game1, game1Defines.empty_var  = game1Defines.communication.button_state(data)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:#only event to handle is quit
                game1Defines.is_game_running = False
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                if pause_rect.collidepoint(event.pos):
                    print("1 Toggle Back")
                    game1Defines.is_game_running = False
                    #menu_selection.display_menu(2)

        # Controls for player movement
        #if keys[pygame.K_LEFT] and player_1_x_position > 0:
        if game1Defines.left_button_pressed_game1 and game1Defines.player_1_x_position > 0:
            game1Defines.player_1_x_position -= game1Defines.player_1_speed
            game1Defines.left_button_pressed_game1 = False
            
        #if keys[pygame.K_RIGHT] and player_1_x_position < screen_width - player_1_width:
        if game1Defines.right_button_pressed_game1 and game1Defines.player_1_x_position > 0:
            game1Defines.player_1_x_position += game1Defines.player_1_speed
            game1Defines.right_button_pressed_game1 = False

        # Moving the enemy
        game1Defines.enemy_1_y_position += game1Defines.enemy_1_speed

        # Check and validate a collision
        if (game1Defines.player_1_x_position < game1Defines.enemy_1_x_position + game1Defines.enemy_1_width and game1Defines.player_1_x_position + game1Defines.player_1_width > game1Defines.enemy_1_x_position
                and game1Defines.player_1_y_position < game1Defines.enemy_1_y_position + game1Defines.enemy_1_height and game1Defines.player_1_y_position + game1Defines.player_1_height > game1Defines.enemy_1_y_position):
            game1Defines.enemy_1_x_position = random.randint(0, game1Defines.screen_width - game1Defines.enemy_1_width)
            game1Defines.enemy_1_y_position = 0
            score += 1

        # Draw screen for game
        game1Defines.screen.fill((0, 0, 0))

        pygame.draw.rect(game1Defines.screen, game1Defines.player_1_color, (game1Defines.player_1_x_position, game1Defines.player_1_y_position, game1Defines.player_1_width, game1Defines.player_1_height))
        pygame.draw.rect(game1Defines.screen, game1Defines.enemy_1_color, (game1Defines.enemy_1_x_position, game1Defines.enemy_1_y_position, game1Defines.enemy_1_width, game1Defines.enemy_1_height))

        score_text = game1Defines.score_font.render("Score: " + str(game1Defines.score), True, (255, 255, 255))

        pause_text = game1Defines.pause_font.render("|| ", True, (100, 100, 100))
        pause_rect = pause_text.get_rect()
        pause_rect.topright = (game1Defines.screen_width - 10, 10)
        
        # Draw All Needed Text
        game1Defines.screen.blit(score_text, (10, 10))
        game1Defines.screen.blit(pause_text, pause_rect)
        
        #Update Screen
        pygame.display.flip()

        # Frame of game 60hz
        game1Defines.clock.tick(60)

    #pygame.display.iconify()
    
