import tkinter as tk


class Move_the_ball(tk.Frame):
    def __init__(self):
        win = tk.Tk()  # Create a tkinter frame or window
        win.title("-   Move The Ball [Basso™]  -")
        win.geometry("700x360")  # Set the size of the window
        win.resizable(False, False)  # Make the window size fixed

        """Variables"""

        self.speed = 10  # Adjust the speed of the ball
        self.x = 305  # Adjust the X-starting point of ball
        self.y = 110  # Adjust the Y-starting point of ball

        """End Variables"""

        # Create a Canvas widget and a ball
        self.canvas = tk.Canvas(win, width=700, height=290)
        self.canvas.pack()
        self.ball = self.canvas.create_oval(20, 20, 60, 60, fill="green3")
        self.canvas.move(self.ball, self.x, self.y)

        # Create a Buttons widget
        frame1 = tk.Frame(win)
        frame1.pack()
        up = tk.Button(frame1, text="Up", width=4, command=self.move_ball_up)
        down = tk.Button(frame1, text="Down", command=self.move_ball_down)
        left = tk.Button(frame1, text="Left", command=self.move_ball_left)
        right = tk.Button(frame1, text="Right", command=self.move_ball_right)
        up.grid(row=3, column=2)
        down.grid(row=4, column=2)
        left.grid(row=4, column=1)
        right.grid(row=4, column=3)

        # Binding arrow-keys
        win.bind("<KeyPress-Left>", self.move_ball_left)
        win.bind("<KeyPress-Right>", self.move_ball_right)
        win.bind("<KeyPress-Up>", self.move_ball_up)
        win.bind("<KeyPress-Down>", self.move_ball_down)

        win.mainloop()

    # Moves the ball in given direction
    def move_ball_left(self, event=None):
        (leftpos, toppos, rightpos, bottompos) = self.canvas.coords(self.ball)
        if leftpos > 5:
            self.canvas.move(self.ball, -self.speed, 0)

    def move_ball_right(self, event=None):
        (leftpos, toppos, rightpos, bottompos) = self.canvas.coords(self.ball)
        if rightpos < 695:
            self.canvas.move(self.ball, self.speed, 0)

    def move_ball_up(self, event=None):
        (leftpos, toppos, rightpos, bottompos) = self.canvas.coords(self.ball)
        if toppos > 5:
            self.canvas.move(self.ball, 0, -self.speed)

    def move_ball_down(self, event=None):
        (leftpos, toppos, rightpos, bottompos) = self.canvas.coords(self.ball)
        if bottompos < 289:
            self.canvas.move(self.ball, 0, self.speed)


if __name__ == "__main__":
    Move_the_ball()
