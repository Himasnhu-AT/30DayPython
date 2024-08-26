
# Python test cases for Day 30

import os
import subprocess
import re
import unittest

class TestDay30(unittest.TestCase):

    def test_game_start(self):
        """Tests whether the game starts with the correct prompt."""
        file_path = os.path.join(os.path.dirname(__file__), "day30.py")
        output = subprocess.check_output(["python", file_path], encoding="utf-8")
        self.assertIn("Welcome to", output)

    def test_user_input(self):
        """Tests whether the game takes user input."""
        file_path = os.path.join(os.path.dirname(__file__), "day30.py")
        with subprocess.Popen(["python", file_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding="utf-8") as process:
            process.stdin.write("go north\n")
            process.stdin.flush()
            output = process.stdout.readline()
            self.assertIn("You go north", output)

    def test_game_logic(self):
        """Tests basic game logic (e.g., moving to a new location)."""
        file_path = os.path.join(os.path.dirname(__file__), "day30.py")
        with subprocess.Popen(["python", file_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding="utf-8") as process:
            process.stdin.write("go north\n")
            process.stdin.flush()
            output = process.stdout.readline()
            self.assertIn("You are now in", output)  # Test if the player moved to a new location

    def test_inventory(self):
        """Tests if the game allows for inventory management."""
        file_path = os.path.join(os.path.dirname(__file__), "day30.py")
        with subprocess.Popen(["python", file_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding="utf-8") as process:
            process.stdin.write("take sword\n")
            process.stdin.flush()
            output = process.stdout.readline()
            self.assertIn("You take the sword", output)  # Test if the player picks up an item
            process.stdin.write("inventory\n")
            process.stdin.flush()
            output = process.stdout.readline()
            self.assertIn("sword", output) # Test if the inventory output is correct

    def test_interactions(self):
        """Tests if the game has interactions with characters."""
        file_path = os.path.join(os.path.dirname(__file__), "day30.py")
        with subprocess.Popen(["python", file_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding="utf-8") as process:
            process.stdin.write("talk to guard\n")
            process.stdin.flush()
            output = process.stdout.readline()
            self.assertIn("Guard:", output)  # Test if the player successfully interacted with a character
            

if __name__ == '__main__':
    unittest.main()

