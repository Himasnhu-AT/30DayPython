
import pygame

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Simple Game")

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
    # ... YOUR CODE HERE ...

    # Drawing
    # ... YOUR CODE HERE ...

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
