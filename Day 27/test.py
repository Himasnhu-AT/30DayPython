
# Python test cases for Day 27

import os
import subprocess
import re

file_path = os.path.join(os.path.dirname(__file__), "day27.py")

# Read the content of day27.py
with open(file_path, "r", encoding="utf-8") as file:
    file_content = file.read()

# Regex pattern to check for the game loop
game_loop_pattern = r"while\s+game_running\s*:"

try:
    # Ensure the game loop is present
    if not re.search(game_loop_pattern, file_content):
        raise AssertionError('The game loop (using a "while" statement) should be present.')

    print("Day 27 game loop test passed successfully!")

    # Check the script's output
    output = subprocess.check_output(["python", file_path], encoding="utf-8")

    # Check if the output includes the initial game state
    if "You are standing at the entrance of a dark forest." not in output:
        raise AssertionError('The initial game state should be printed (e.g., "You are standing at the entrance of a dark forest.")')

    # Check if the output includes an option to move forward
    if "Press 'f' to move forward or 'q' to quit" not in output:
        raise AssertionError('The output should include an option to move forward or quit.')

    print("Day 27 output test passed successfully!")

except Exception as error:
    print("Day 27 tests failed!")
    print(str(error))
    sys.exit(1)

