import pygame
import random
import communication
import serial

# Initialize pygame
pygame.init()

# Set up the screen
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders from Wish")

# Set up the clock
clock = pygame.time.Clock()

# Set up the player
player_image = pygame.image.load("assets/player.png")
player_width = 64
player_height = 64
player_x = (screen_width - player_width) // 2
player_y = screen_height - player_height - 10
player_speed = 15

left_button_press_spaceGame = False
right_button_press_spaceGame = False
attack_button_press_spaceGame = False

# Set up the bullets
bullet_image = pygame.image.load("assets/bullet.png")
bullet_width = 16
bullet_height = 32
bullet_speed = 10
bullet_list = []

# Set up the enemies
enemy_image = pygame.image.load("assets/enemy.png")
enemy_width = 64
enemy_height = 64
enemy_speed = 2
enemy_list = []
for i in range(5):
    enemy_x = random.randint(0, screen_width - enemy_width)
    enemy_y = random.randint(-200, -enemy_height)
    enemy_list.append((enemy_x, enemy_y))

### Set Up Connection to Arduino ###
arduino1 = serial.Serial('COM3', 9600)


# Set up the game loop
running = True
while running:
    if arduino1.in_waiting > 0:
        # read data from serial connection
        data = arduino1.read().decode('utf-8')
        # handle incoming data here
        print('Received character: {}'.format(data))
        print('Received Type: ', type(data))
        left_button_press_spaceGame, right_button_press_spaceGame, attack_button_press_spaceGame  = communication.button_state(data)
        
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         bullet_x = player_x + (player_width - bullet_width) // 2
        #         bullet_y = player_y - bullet_height
        #         bullet_list.append((bullet_x, bullet_y))
        #         attack_button_press_spaceGame = False

    # Handle player movement and bullet attack
    if left_button_press_spaceGame and player_x > 0:
        player_x -= player_speed
        left_button_press_spaceGame = False

    elif right_button_press_spaceGame and player_x < screen_width - player_width:
        player_x += player_speed
        right_button_press_spaceGame = False

    elif attack_button_press_spaceGame:
        bullet_x = player_x + (player_width - bullet_width) // 2
        bullet_y = player_y - bullet_height
        bullet_list.append((bullet_x, bullet_y))
        attack_button_press_spaceGame = False

    # Handle bullet movement
    for i, bullet in enumerate(bullet_list):
        bullet_x, bullet_y = bullet
        bullet_y -= bullet_speed
        if bullet_y < -bullet_height:
            bullet_list.pop(i)
        else:
            bullet_list[i] = (bullet_x, bullet_y)

    # Handle enemy movement
    for i, enemy in enumerate(enemy_list):
        enemy_x, enemy_y = enemy
        enemy_y += enemy_speed
        if enemy_y > screen_height:
            enemy_x = random.randint(0, screen_width - enemy_width)
            enemy_y = random.randint(-200, -enemy_height)
        enemy_list[i] = (enemy_x, enemy_y)

    # Handle collisions
    for enemy in enemy_list:
        enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_width, enemy_height)
        for bullet in bullet_list:
            bullet_rect = pygame.Rect(bullet[0], bullet[1], bullet_width, bullet_height)
            if enemy_rect.colliderect(bullet_rect):
                enemy_x = random.randint(0, screen_width - enemy_width)
                enemy_y = random.randint(-200, -enemy_height)
                enemy_list[enemy_list.index(enemy)] = (enemy_x, enemy_y)
                bullet_list.remove(bullet)

    # Load and scale the enemy image
    enemy_image = pygame.image.load("assets/enemy.png")
    enemy_width = 64
    enemy_height = 64
    enemy_image = pygame.transform.scale(enemy_image, (enemy_width, enemy_height))

    #Kelvin: trying to resize the player
    player_image = pygame.image.load("assets/player.png")
    player_width = 64
    player_height = 64
    player_image = pygame.transform.scale(player_image, (player_width, player_height))

    #Kelvin: trying to resize the bullet
    bullet_image = pygame.image.load("assets/bullet.png")
    bullet_width = 64
    bullet_height = 64
    bullet_image = pygame.transform.scale(bullet_image, (bullet_width, bullet_height))          

    # Draw everything
    screen.fill((0, 0, 0))
    screen.blit(player_image, (player_x, player_y))
    for bullet in bullet_list:
        screen.blit(bullet_image, bullet)
    for enemy in enemy_list:
        screen.blit(enemy_image, enemy)

    pygame.display.flip()
