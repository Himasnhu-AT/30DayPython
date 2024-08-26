
# Day 24: Tkinter GUI Tests

import unittest
from tkinter import Tk, Button, Label, Entry, StringVar, messagebox
from day24 import create_simple_window, handle_button_click, create_input_window, handle_entry_input

class Day24Tests(unittest.TestCase):

    def test_create_simple_window(self):
        """Tests if the window is created with the correct title and size."""
        root = Tk()
        create_simple_window(root)
        self.assertEqual(root.title(), "Simple Tkinter Window")
        self.assertEqual(root.winfo_width(), 300)
        self.assertEqual(root.winfo_height(), 200)
        root.destroy()

    def test_handle_button_click(self):
        """Tests if the button click handler changes the label text."""
        root = Tk()
        label = Label(root, text="Initial Text")
        label.pack()
        button = Button(root, text="Click Me", command=lambda: handle_button_click(label))
        button.pack()
        button.invoke()  # Simulate button click
        self.assertEqual(label.cget("text"), "Button Clicked!")
        root.destroy()

    def test_create_input_window(self):
        """Tests if the input window is created with the correct elements."""
        root = Tk()
        create_input_window(root)
        self.assertIsInstance(root.children["!entry"], Entry)
        self.assertIsInstance(root.children["!label"], Label)
        self.assertIsInstance(root.children["!button"], Button)
        root.destroy()

    def test_handle_entry_input(self):
        """Tests if the entry input is processed correctly."""
        root = Tk()
        entry_var = StringVar()
        entry = Entry(root, textvariable=entry_var)
        entry.pack()
        button = Button(root, text="Submit", command=lambda: handle_entry_input(entry_var))
        button.pack()
        entry_var.set("Test Input")
        button.invoke()  # Simulate button click
        self.assertEqual(messagebox.showinfo("Input Received", "You entered: Test Input"), "ok")
        root.destroy()

if __name__ == '__main__':
    unittest.main()

