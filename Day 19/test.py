
# Python test cases for Day 19

import os
import subprocess
import re

file_path = os.path.join(os.path.dirname(__file__), "day19.py")

# Read the content of day19.py
with open(file_path, "r", encoding="utf-8") as file:
    file_content = file.read()

# Regex pattern to check if Matplotlib is imported
import_pattern = r"import matplotlib\.pyplot as plt"

try:
    # Ensure Matplotlib is imported
    if not re.search(import_pattern, file_content):
        raise AssertionError('The script should import Matplotlib using "import matplotlib.pyplot as plt"')

    print("Day 19 import test passed successfully!")

    # Check the script's output (a plot file should be generated)
    subprocess.check_output(["python", file_path], encoding="utf-8")

    # Verify the existence of the plot file
    plot_file = os.path.join(os.path.dirname(__file__), "day19_plot.png")
    if not os.path.exists(plot_file):
        raise AssertionError("The script should generate a plot file named 'day19_plot.png'")

    print("Day 19 plot generation test passed successfully!")

except Exception as error:
    print("Day 19 tests failed!")
    print(str(error))
    sys.exit(1)

