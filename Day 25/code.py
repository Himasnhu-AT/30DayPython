
# Day 25: Code implementation for Tkinter GUI application

import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Simple GUI App")

# Create a label widget
label = tk.Label(window, text="Hello from Tkinter!")
label.pack()

# Create a button widget
button = tk.Button(window, text="Click Me")
button.pack()

# Start the GUI event loop
window.mainloop()

