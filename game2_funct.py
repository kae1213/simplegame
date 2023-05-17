import game2Defines
import serial
import pygame
from pygame.locals import *
import random

def initGame2():
    arduino1 = serial.Serial('COM3', 9600)
    # Game logic to start
    while game2Defines.is_game_running:
        if arduino1.in_waiting > 0:
            # read data from serial connection
            data = arduino1.read().decode('utf-8')
            # handle incoming data here
            print('Received character: {}'.format(data))
            print('Received Type: ', type(data))
            game2Defines.left_button_press_spaceGame, game2Defines.right_button_press_spaceGame, game2Defines.attack_button_press_spaceGame  = game2Defines.communication.button_state(data)
            
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game2Defines.is_game_running = False
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                if pause_rect.collidepoint(event.pos):
                    print("2 Toggle Back")
                    game2Defines.is_game_running = False
                    
        # Handle player movement and bullet attack
        if game2Defines.left_button_press_spaceGame and game2Defines.player_x_position > 0:
            game2Defines.player_x_position -= game2Defines.player_speed
            game2Defines.left_button_press_spaceGame = False

        elif game2Defines.right_button_press_spaceGame and game2Defines.player_x_position < game2Defines.screen_width - game2Defines.player_width:
            game2Defines.player_x_position += game2Defines.player_speed
            game2Defines.right_button_press_spaceGame = False

        elif game2Defines.attack_button_press_spaceGame:
            game2Defines.bullet_x = game2Defines.player_x_position + (game2Defines.player_width - game2Defines.bullet_width) // 2
            game2Defines.bullet_y = game2Defines.player_y_position - game2Defines.bullet_height
            game2Defines.bullet_list.append((game2Defines.bullet_x, game2Defines.bullet_y))
            game2Defines.attack_button_press_spaceGame = False

        # Handle bullet movement
        for i, bullet in enumerate(game2Defines.bullet_list):
            game2Defines.bullet_x, game2Defines.bullet_y = game2Defines.bullet
            game2Defines.bullet_y -= game2Defines.bullet_speed
            if game2Defines.bullet_y < -game2Defines.bullet_height:
                game2Defines.bullet_list.pop(i)
            else:
                game2Defines.bullet_list[i] = (game2Defines.bullet_x, game2Defines.bullet_y)

        # Handle enemy movement
        for i, enemy in enumerate(game2Defines.enemy_list):
            game2Defines.enemy_x, enemy_y = enemy
            game2Defines.enemy_y += game2Defines.enemy_speed
            if game2Defines.enemy_y > game2Defines.screen_height:
                game2Defines.enemy_x = random.randint(0, game2Defines.screen_width - game2Defines.enemy_width)
                game2Defines.enemy_y = random.randint(-200, -game2Defines.enemy_height)
            game2Defines.enemy_list[i] = (game2Defines.enemy_x, game2Defines.enemy_y)

        # Handle collisions
        for enemy in game2Defines.enemy_list:
            enemy_rect = pygame.Rect(enemy[0], enemy[1], game2Defines.enemy_width, game2Defines.enemy_height)
            for bullet in game2Defines.bullet_list:
                bullet_rect = pygame.Rect(bullet[0], bullet[1], game2Defines.bullet_width, game2Defines.bullet_height)
                if enemy_rect.colliderect(bullet_rect):
                    game2Defines.enemy_x = random.randint(0, game2Defines.screen_width - game2Defines.enemy_width)
                    game2Defines.enemy_y = random.randint(-200, -game2Defines.enemy_height)
                    game2Defines.enemy_list[game2Defines.enemy_list.index(enemy)] = (game2Defines.enemy_x, game2Defines.enemy_y)
                    game2Defines.bullet_list.remove(bullet)

        # Load and scale the enemy image
        game2Defines.enemy_image = pygame.image.load("assets/enemy.png")
        game2Defines.enemy_width = 64
        game2Defines.enemy_height = 64
        game2Defines.enemy_image = pygame.transform.scale(game2Defines.enemy_image, (game2Defines.enemy_width, game2Defines.enemy_height))

        #Kelvin: trying to resize the player
        game2Defines.player_image = pygame.image.load("assets/player.png")
        game2Defines.player_width = 64
        game2Defines.player_height = 64
        game2Defines.player_image = pygame.transform.scale(game2Defines.player_image, (game2Defines.player_width, game2Defines.player_height))

        #Kelvin: trying to resize the bullet
        game2Defines.bullet_image = pygame.image.load("assets/bullet.png")
        game2Defines.bullet_width = 64
        game2Defines.bullet_height = 64
        game2Defines.bullet_image = pygame.transform.scale(game2Defines.bullet_image, (game2Defines.bullet_width, game2Defines.bullet_height))          

        # Draw section for Pause
        pause_text = game2Defines.pause_font.render("|| ", True, (100, 100, 100))
        pause_rect = pause_text.get_rect()
        pause_rect.topright = (game2Defines.screen_width - 10, 10)

        # Draw everything
        game2Defines.screen.fill((0, 0, 0))
        game2Defines.screen.blit(game2Defines.player_image, (game2Defines.player_x_position, game2Defines.player_y_position))
        game2Defines.screen.blit(pause_text, pause_rect)

        for bullet in game2Defines.bullet_list:
            game2Defines.screen.blit(game2Defines.bullet_image, bullet)
        for enemy in game2Defines.enemy_list:
            game2Defines.screen.blit(game2Defines.enemy_image, enemy)

        pygame.display.flip()


