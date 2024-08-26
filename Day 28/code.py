
import pygame

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Pygame Game")

# Load background image
background_image = pygame.image.load("background.png").convert()

# Load player image
player_image = pygame.image.load("player.png").convert_alpha()
player_x = screen_width // 2
player_y = screen_height // 2

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic (update player position, etc.)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5
    if keys[pygame.K_UP]:
        player_y -= 5
    if keys[pygame.K_DOWN]:
        player_y += 5

    # Drawing
    screen.blit(background_image, (0, 0))
    screen.blit(player_image, (player_x, player_y))

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

