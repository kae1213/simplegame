import game3Defines
import pygame
from pygame.locals import *
import random
import serial

def initGame3():
    arduino1 = serial.Serial('COM3', 9600)
    arduino1.timeout = 1  # Set a timeout value in seconds
    arduino1.readline()  # Read a line from the serial port 
    if(arduino1):
        arduino1.write(game3Defines.startGame.encode())  # Convert data to bytes and send it
        #arduino1.write('B'.encode())
        print('hold')
    while game3Defines.is_game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#only event to handle is quit
                arduino1.write(game3Defines.endGame.encode())  # Convert data to bytes and send it
                game3Defines.is_game_running = False

            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                if pause_rect.collidepoint(event.pos):
                    print("3 Toggle Back")
                    game3Defines.is_game_running = False
                    arduino1.write(game3Defines.endGame.encode())  # Convert data to bytes and send it
        
        pause_text = game3Defines.pause_font.render("|| ", True, (100, 100, 100))
        pause_rect = pause_text.get_rect()
        pause_rect.topright = (game3Defines.screen_width - 10, 10)

        # Draw screen for game
        game3Defines.screen.fill((0, 0, 0))
        
        # Draw All Needed Text
        
        game3Defines.screen.blit(pause_text, pause_rect)

        pygame.display.flip()
        game3Defines.clock.tick(60)
