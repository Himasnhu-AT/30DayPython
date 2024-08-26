
import unittest
import pygame
import sys
import os

# Assuming your game file is named "day28_game.py"
game_file = "day28_game.py"

class TestDay28Game(unittest.TestCase):

    def setUp(self):
        # Initialize Pygame for testing
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Day 28 Game Test")

    def test_game_loop(self):
        """Tests if the game loop runs and handles events."""
        try:
            # Run the game file 
            exec(open(game_file).read(), globals())
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
        except Exception as e:
            self.fail(f"Error running the game: {e}")

    def tearDown(self):
        # Quit Pygame after testing
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    unittest.main()

