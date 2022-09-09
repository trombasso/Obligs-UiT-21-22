from math import sqrt
import tkinter as tk


win = tk.Tk()
win.geometry("700x350")
win.title("")
win.resizable(False, False)

canvas = tk.Canvas(win, width=700, height=350, bg="white")
canvas.pack(pady=0)

# Size, X and Y coordinates of startpos for both circles

RADIUS = 20
RED_BALL_C = [100, 100]
BLUE_BALL_C = [350, 200]
LINE_THICKNESS = 1
MIN_DISTANCE = 70

# -------------------------------------------------------


red_ball = tk.Canvas.create_oval(
    canvas,
    RED_BALL_C[0] - RADIUS,
    RED_BALL_C[1] - RADIUS,
    RED_BALL_C[0] + RADIUS,
    RED_BALL_C[1] + RADIUS,
    fill="red",
    outline="black",
    width=LINE_THICKNESS,
)
blue_ball = tk.Canvas.create_oval(
    canvas,
    BLUE_BALL_C[0] - RADIUS,
    BLUE_BALL_C[1] - RADIUS,
    BLUE_BALL_C[0] + RADIUS,
    BLUE_BALL_C[1] + RADIUS,
    fill="blue",
    outline="black",
    width=LINE_THICKNESS,
)
line = tk.Canvas.create_line(canvas, RED_BALL_C[0], RED_BALL_C[1], BLUE_BALL_C[0], BLUE_BALL_C[1], fill="black", width=LINE_THICKNESS)
linelength = sqrt((canvas.coords(line)[1] - canvas.coords(line)[3]) ** 2 + (canvas.coords(line)[0] - canvas.coords(line)[2]) ** 2)
linelength_text = tk.Canvas.create_text(
    canvas,
    RED_BALL_C[0] + ((BLUE_BALL_C[0] - RED_BALL_C[0]) // 2),
    RED_BALL_C[1] + ((BLUE_BALL_C[1] - RED_BALL_C[1]) // 2),
    text=f"{linelength:.2f}",
    fill="black",
)


# Define a function to allow the balls to move within the canvas
def move(e):
    global red_ball, blue_ball, line, linelength_text

    linelength = sqrt((canvas.coords(line)[1] - canvas.coords(line)[3]) ** 2 + (canvas.coords(line)[0] - canvas.coords(line)[2]) ** 2)
    # hyp = sqrt( )
    cursordistance_red = sqrt((e.y - canvas.coords(line)[3]) ** 2 + ((e.x - canvas.coords(line)[2]) ** 2))
    cursordistance_blue = sqrt((e.y - canvas.coords(line)[1]) ** 2 + ((e.x - canvas.coords(line)[0]) ** 2))

    if (
        e.x > canvas.coords(red_ball)[0]
        and e.y > canvas.coords(red_ball)[1]
        and e.x < canvas.coords(red_ball)[0] + RADIUS * 2
        and e.y < canvas.coords(red_ball)[1] + RADIUS * 2
        and cursordistance_red > MIN_DISTANCE
    ):
        canvas.delete(red_ball)
        canvas.delete(line)
        canvas.delete(linelength_text)
        red_ball = canvas.create_oval(
            e.x - RADIUS, e.y - RADIUS, e.x + RADIUS, e.y + RADIUS, fill="red", outline="black", width=LINE_THICKNESS
        )
        line = canvas.create_line(
            e.x, e.y, canvas.coords(blue_ball)[0] + RADIUS, canvas.coords(blue_ball)[1] + RADIUS, fill="black", width=LINE_THICKNESS
        )
        linelength_text = tk.Canvas.create_text(
            canvas,
            canvas.coords(line)[0] + ((canvas.coords(line)[2] - canvas.coords(line)[0]) // 2),
            canvas.coords(line)[1] + ((canvas.coords(line)[3] - canvas.coords(line)[1]) // 2),
            text=f"{linelength:.2f}",
            fill="black",
        )

    elif (
        e.x > canvas.coords(blue_ball)[0]
        and e.y > canvas.coords(blue_ball)[1]
        and e.x < canvas.coords(blue_ball)[0] + RADIUS * 2
        and e.y < canvas.coords(blue_ball)[1] + RADIUS * 2
        and cursordistance_blue > MIN_DISTANCE
    ):
        canvas.delete(blue_ball)
        canvas.delete(line)
        canvas.delete(linelength_text)
        blue_ball = canvas.create_oval(
            e.x - RADIUS, e.y - RADIUS, e.x + RADIUS, e.y + RADIUS, fill="blue", outline="black", width=LINE_THICKNESS
        )
        line = canvas.create_line(
            canvas.coords(red_ball)[0] + RADIUS, canvas.coords(red_ball)[1] + RADIUS, e.x, e.y, fill="black", width=LINE_THICKNESS
        )
        linelength_text = tk.Canvas.create_text(
            canvas,
            canvas.coords(line)[0] + ((canvas.coords(line)[2] - canvas.coords(line)[0]) // 2),
            canvas.coords(line)[1] + ((canvas.coords(line)[3] - canvas.coords(line)[1]) // 2),
            text=f"{linelength:.2f}",
            fill="black",
        )


# Bind the move function
canvas.bind("<B1-Motion>", move)

win.mainloop()
