import tkinter as tk

# Moves the ball in given direction
def move_ball_left(event=None):
    (leftpos, toppos, rightpos, bottompos) = canvas.coords(ball)
    if leftpos > 0:
        canvas.move(ball, -3, 0)


def move_ball_right(event=None):
    (leftpos, toppos, rightpos, bottompos) = canvas.coords(ball)
    if rightpos < 700:
        canvas.move(ball, 3, 0)


def move_ball_up(event=None):
    (leftpos, toppos, rightpos, bottompos) = canvas.coords(ball)
    if toppos > 0:
        canvas.move(ball, 0, -3)


def move_ball_down(event=None):
    (leftpos, toppos, rightpos, bottompos) = canvas.coords(ball)
    if bottompos < 280:
        canvas.move(ball, 0, 3)


win = tk.Tk()  # Create a tkinter master frame
win.geometry("700x350")  # Set the size of the window
win.resizable(False, False)  # Make the window size fixed

# Create a canvas widget
canvas = tk.Canvas(win, width=700, height=280, bg="white")
canvas.pack()
# Create an oval or ball in the canvas widget
ball = canvas.create_oval(20, 20, 60, 60, fill="green3")  

# Create a Buttons widget
frame1 = tk.Frame(win)
frame1.pack()
up = tk.Button(frame1, text="Up", command=move_ball_up)
down = tk.Button(frame1, text="Down", command=move_ball_down)
left = tk.Button(frame1, text="Left", command=move_ball_left)
right = tk.Button(frame1, text="Right", command=move_ball_right)
up.grid(row=3, column=2)
down.grid(row=4, column=2)
left.grid(row=4, column=1)
right.grid(row=4, column=3)

# Binding arrow-keys
win.bind("<KeyPress-Left>", move_ball_left)
win.bind("<KeyPress-Right>", move_ball_right)
win.bind("<KeyPress-Up>", move_ball_up)
win.bind("<KeyPress-Down>", move_ball_down)


win.mainloop()
