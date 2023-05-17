import menu_selection
import pygame
from pygame.locals import *

##################################################################
######################   Main Function   #########################
##################################################################

# Will wake menu selection window, controlled through PC keybaord
def main():
    selected_option = 1
    menu_selection.display_menu(selected_option)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    selected_option = max(1, selected_option - 1)
                elif event.key == K_DOWN:
                    selected_option = min(3, selected_option + 1)
                elif event.key == K_RETURN:
                # Case once enter is pressed
                    if selected_option == 1:
                        menu_selection.game1()
                    elif selected_option == 2:
                        menu_selection.game2()
                    elif selected_option == 3:
                        menu_selection.game3()
        
        menu_selection.display_menu(selected_option)       

if __name__ == '__main__':
    main()