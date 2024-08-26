
/* Day 24: Let's create a simple GUI with Tkinter.
 *
 *  **Task 1**: Create a basic window with the title "My First GUI".
 *  **Task 2**: Add a button labeled "Click Me" and a label that initially displays "Hello!".
 *  **Task 3**:  Implement a function that handles the button click and changes the label text to "Button Clicked!".
 *
 * LICENSE: ALL RIGHTS RESERVED (C) 2024 @OpenEdu <git: openeduhq> @Himanshu <git: himanshu-at>
 *
 **/

from tkinter import Tk, Button, Label

def create_gui(root):
    """Creates the main GUI window."""
    # Set the window title
    root.title("My First GUI")

    # Add a label to the window
    label = Label(root, text="Hello!")
    label.pack()

    # Add a button to the window
    button = Button(root, text="Click Me", command=lambda: handle_button_click(label))
    button.pack()

def handle_button_click(label):
    """Handles the button click event."""
    # Update the label text to "Button Clicked!"
    label.config(text="Button Clicked!")

if __name__ == "__main__":
    root = Tk()
    create_gui(root)
    root.mainloop()
