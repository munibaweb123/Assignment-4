# Problem Statement
# Implement an 'eraser' on a canvas.

# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.

import tkinter as tk

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser):
    """Erase objects in contact with the eraser."""
    # Get mouse position relative to canvas
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    
    # Define eraser bounds
    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE
    
    # Find overlapping objects
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
    
    # Set overlapping objects to white (erase effect)
    for obj in overlapping_objects:
        if obj != eraser:
            canvas.itemconfig(obj, fill='white')

def move_eraser():
    """Move the eraser with the mouse and erase objects."""
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    
    # Move eraser to the mouse position
    canvas.moveto(eraser, mouse_x, mouse_y)
    
    # Erase objects under eraser
    erase_objects(canvas, eraser)
    
    # Schedule the next update (keep updating)
    root.after(50, move_eraser)

def start_eraser(event):
    """Start erasing when the user clicks."""
    global eraser
    eraser = canvas.create_rectangle(event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE, fill="pink")
    move_eraser()  # Start tracking the eraser movement

# Initialize Tkinter
root = tk.Tk()
root.title("Eraser Grid")

# Create Canvas
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
canvas.pack()

# Create Grid
for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
    for col in range(0, CANVAS_WIDTH, CELL_SIZE):
        canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue")

# Wait for user to click to create eraser
canvas.bind("<Button-1>", start_eraser)

# Start Tkinter loop
root.mainloop()
