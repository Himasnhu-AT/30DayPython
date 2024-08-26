
# Day 25: Test cases for Tkinter GUI application

import os
import subprocess
import time

file_path = os.path.join(os.path.dirname(__file__), "day25.py")

def run_and_check(expected_title, expected_label_text, expected_button_text):
    try:
        # Run the script and wait for the GUI window to appear
        process = subprocess.Popen(["python", file_path])
        time.sleep(2)

        # Check the window title
        output = subprocess.check_output(["xprop", "-id", "(wmctrl -l | grep 'day25' | awk '{print $1}')", "-f", '%s\n', "_NET_WM_NAME"], encoding="utf-8").strip()
        if output != expected_title:
            raise AssertionError(f"Window title mismatch: Expected '{expected_title}', got '{output}'")

        # Check the label text
        output = subprocess.check_output(["xprop", "-id", "(wmctrl -l | grep 'day25' | awk '{print $1}')", "-f", '%s\n', "WM_NAME"], encoding="utf-8").strip()
        if output != expected_label_text:
            raise AssertionError(f"Label text mismatch: Expected '{expected_label_text}', got '{output}'")

        # Check the button text
        output = subprocess.check_output(["xprop", "-id", "(wmctrl -l | grep 'day25' | awk '{print $1}')", "-f", '%s\n', "WM_NAME"], encoding="utf-8").strip()
        if output != expected_button_text:
            raise AssertionError(f"Button text mismatch: Expected '{expected_button_text}', got '{output}'")

        # Send a SIGTERM signal to close the window
        os.kill(process.pid, 15)
        print("Day 25 tests passed successfully!")
    except Exception as error:
        print("Day 25 tests failed!")
        print(str(error))
        sys.exit(1)


run_and_check("Simple GUI App", "Hello from Tkinter!", "Click Me")

