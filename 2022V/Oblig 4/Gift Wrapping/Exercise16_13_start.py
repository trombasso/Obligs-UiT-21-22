import tkinter as tk


from gift_wrapping import getConvexHull


def add(event):
    points.append([event.x, event.y])
    repaint()


def remove(event):
    for [x, y] in points:
        if distance(x, y, event.x, event.y) <= 10:
            points.remove([x, y])
    repaint()


def distance(x, y, x1, y1):
    return ((x - x1) * (x - x1) + (y - y1) * (y - y1)) ** 0.5


def repaint():
    canvas.delete("point")
    if len(points) > 0:
        # H = [[2.5, 2.0], [6.0, 2.4], [5.5, 9.0], [1.5, 34.5], [1.0, 2.4]]
        # pass
        H = getConvexHull(points)  # call GiftWrapping getConvexHull
        canvas.create_polygon(H, fill="gray", tags="point")

    for [x, y] in points:
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, tags="point", fill="black")


def displayInstructions():
    instructions = ["INSTRUCTIONS", "Add:", "Left Click", "Remove:", "Right Click"]
    x = 200
    y = 200
    canvas.create_rectangle(x, y, x + 160, y + 80)
    canvas.create_text(x + 10 + 40, y + 20, text=instructions[0], justify=tk.CENTER)
    for i in range(1, len(instructions), 2):
        canvas.create_text(x + 10 + 40, y + 20 + (i + 1) * 10, text=instructions[i], justify=tk.RIGHT)
        canvas.create_text(x + 80 + 40, y + 20 + (i + 1) * 10, text=instructions[i + 1], justify=tk.RIGHT)


window = tk.Tk()  # Create a window
window.title("Convex Hull")  # Set title

width = 1000
height = 800
radius = 5
canvas = tk.Canvas(window, bg="white", width=width, height=height)
canvas.pack()

# Create a 2-D list for storing points
points = []
displayInstructions()


canvas.bind("<Button-1>", add)
canvas.bind("<Button-2>", remove)


window.mainloop()  # Create an event loop
