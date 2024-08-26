
# Day 24: Tkinter GUI Implementation

from tkinter import Tk, Button, Label, Entry, StringVar, messagebox

def create_simple_window(root):
    """Creates a simple Tkinter window with a button."""
    root.title("Simple Tkinter Window")
    root.geometry("300x200")

    label = Label(root, text="Welcome to Tkinter!")
    label.pack()

    button = Button(root, text="Click Me", command=lambda: handle_button_click(label))
    button.pack()

def handle_button_click(label):
    """Handles button click event, changing the label text."""
    label.config(text="Button Clicked!")

def create_input_window(root):
    """Creates a window with an entry field and a submit button."""
    root.title("Input Window")
    root.geometry("300x100")

    label = Label(root, text="Enter your name:")
    label.pack()

    entry = Entry(root)
    entry.pack()

    button = Button(root, text="Submit", command=lambda: handle_entry_input(entry.get()))
    button.pack()

def handle_entry_input(entry_text):
    """Handles the submit button click, displaying the input text."""
    messagebox.showinfo("Input Received", f"You entered: {entry_text}")

if __name__ == "__main__":
    root = Tk()
    create_simple_window(root)
    root.mainloop()  # Keep the window running

