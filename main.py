# Import tkinter library
from tkinter import * 

# Create a window with an isntance of Tk(tkinter)
window = Tk()
# Window called WhiteBoard
window.title("WhiteBoard")

# Create a var to store a canvas with our window, width, height  and a colour
canvas = Canvas(window, width = 1800, height = 1000, bg = 'white')
# Pack our widget 
canvas.pack()

# Variables to control if we are drawing, position of the last time we drew
# and the track of the line
drawing = False
lastX = 0
lastY = 0
lineTrack = [] 

# Function that start drawing, updating the boolean variable and last position
def startDrawing(actualPosition):
    global drawing, lastX, lastY
    drawing = True
    lastX = actualPosition.x
    lastY = actualPosition.y
# We are calling a function(startDrawing) when click Button-1
canvas.bind('<Button-1>', startDrawing)

# Function that stops drawing, updating startDrawing
def stopDrawing(actualPosition):
    global drawing
    drawing = False
# When we stop clicking Button1
canvas.bind('<ButtonRelease-1>', stopDrawing)

# Draws, create a line between last position and actual with a line in black
# and store it on our lineTrack list
def draw(actualPosition):
    global lastX, lastY
    if drawing:
        line = canvas.create_line(lastX, lastY, actualPosition.x, actualPosition.y, fill = 'black')
        lineTrack.append(line)
        lastX = actualPosition.x
        lastY = actualPosition.y
# When the mouse is moving
canvas.bind('<B1-Motion>', draw)

# Function that deletes the last line of the lineTrack
def deleteLastLine(actualPosition):
    if lineTrack:
        canvas.delete(lineTrack.pop())
# Create a shortcut for CTRL+Z to remove lines, this one will be asociated 
# to our window and not to our canvas(like previously)
window.bind('<Control-z>', deleteLastLine)

# Loop our window(method form tkinter library)
window.mainloop()