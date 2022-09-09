import tkinter as tk
import tkinter.messagebox

root = tk.Tk()
root.title("-   TicTacToe   -")
root.tk.call("wm", "iconphoto", root._w, tk.PhotoImage(file="assets/tictactoe.png"))
root.resizable(False, False)

click = True
count = 0


game = tk.Frame()
game.pack()


btn1 = tk.StringVar()
btn2 = tk.StringVar()
btn3 = tk.StringVar()
btn4 = tk.StringVar()
btn5 = tk.StringVar()
btn6 = tk.StringVar()
btn7 = tk.StringVar()
btn8 = tk.StringVar()
btn9 = tk.StringVar()
xwins = tk.IntVar()
owins = tk.IntVar()


x_image = tk.PhotoImage(file="assets/cross.png")
o_image = tk.PhotoImage(file="assets/circle.png")
e_image = tk.PhotoImage(file="assets/empty.png")


def play():
    button1 = tk.Button(game, bd=0, relief="flat", image=e_image, textvariable=btn1, command=lambda: press(1, 0, 0))
    button2 = tk.Button(game, bd=0, relief="flat", image=e_image, textvariable=btn2, command=lambda: press(2, 0, 1))
    button3 = tk.Button(game, bd=0, relief="flat", image=e_image, textvariable=btn3, command=lambda: press(3, 0, 2))
    button4 = tk.Button(game, bd=0, relief="flat", image=e_image, textvariable=btn4, command=lambda: press(4, 1, 0))
    button5 = tk.Button(game, bd=0, relief="flat", image=e_image, textvariable=btn5, command=lambda: press(5, 1, 1))
    button6 = tk.Button(game, bd=0, relief="flat", image=e_image, textvariable=btn6, command=lambda: press(6, 1, 2))
    button7 = tk.Button(game, bd=0, relief="flat", image=e_image, textvariable=btn7, command=lambda: press(7, 2, 0))
    button8 = tk.Button(game, bd=0, relief="flat", image=e_image, textvariable=btn8, command=lambda: press(8, 2, 1))
    button9 = tk.Button(game, bd=0, relief="flat", image=e_image, textvariable=btn9, command=lambda: press(9, 2, 2))

    button1.grid(row=0, column=0)
    button2.grid(row=0, column=1)
    button3.grid(row=0, column=2)
    button4.grid(row=1, column=0)
    button5.grid(row=1, column=1)
    button6.grid(row=1, column=2)
    button7.grid(row=2, column=0)
    button8.grid(row=2, column=1)
    button9.grid(row=2, column=2)


def press(num, r, c):
    global click, count
    if click is True:
        labelPhoto = tk.Label(game, image=x_image)
        labelPhoto.grid(row=r, column=c)
        if num == 1:
            btn1.set("X")
        elif num == 2:
            btn2.set("X")
        elif num == 3:
            btn3.set("X")
        elif num == 4:
            btn4.set("X")
        elif num == 5:
            btn5.set("X")
        elif num == 6:
            btn6.set("X")
        elif num == 7:
            btn7.set("X")
        elif num == 8:
            btn8.set("X")
        else:
            btn9.set("X")
        count += 1
        click = False
        game.update()
        checkWin()

    else:
        labelPhoto = tk.Label(game, image=o_image)
        labelPhoto.grid(row=r, column=c)
        if num == 1:
            btn1.set("O")
        elif num == 2:
            btn2.set("O")
        elif num == 3:
            btn3.set("O")
        elif num == 4:
            btn4.set("O")
        elif num == 5:
            btn5.set("O")
        elif num == 6:
            btn6.set("O")
        elif num == 7:
            btn7.set("O")
        elif num == 8:
            btn8.set("O")
        else:
            btn9.set("O")
        count += 1
        click = True
        game.update()
        checkWin()


def checkWin():
    global count, click
    if (
        btn1.get() == "X"
        and btn2.get() == "X"
        and btn3.get() == "X"
        or btn4.get() == "X"
        and btn5.get() == "X"
        and btn6.get() == "X"
        or btn7.get() == "X"
        and btn8.get() == "X"
        and btn9.get() == "X"
        or btn1.get() == "X"
        and btn4.get() == "X"
        and btn7.get() == "X"
        or btn2.get() == "X"
        and btn5.get() == "X"
        and btn8.get() == "X"
        or btn3.get() == "X"
        and btn6.get() == "X"
        and btn9.get() == "X"
        or btn1.get() == "X"
        and btn5.get() == "X"
        and btn9.get() == "X"
        or btn3.get() == "X"
        and btn5.get() == "X"
        and btn7.get() == "X"
    ):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "X wins the game!")
        click = True
        count = 0
        clear()
        play()

    elif (
        btn1.get() == "O"
        and btn2.get() == "O"
        and btn3.get() == "O"
        or btn4.get() == "O"
        and btn5.get() == "O"
        and btn6.get() == "O"
        or btn7.get() == "O"
        and btn8.get() == "O"
        and btn9.get() == "O"
        or btn1.get() == "O"
        and btn4.get() == "O"
        and btn7.get() == "O"
        or btn2.get() == "O"
        and btn5.get() == "O"
        and btn8.get() == "O"
        or btn3.get() == "O"
        and btn6.get() == "O"
        and btn9.get() == "O"
        or btn1.get() == "O"
        and btn5.get() == "O"
        and btn9.get() == "O"
        or btn3.get() == "O"
        and btn5.get() == "O"
        and btn7.get() == "O"
    ):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "O wins the game!")
        count = 0
        clear()
        play()

    elif count == 9:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Nobody wins!")
        click = True
        count = 0
        clear()
        play()


def clear():
    btn1.set("")
    btn2.set("")
    btn3.set("")
    btn4.set("")
    btn5.set("")
    btn6.set("")
    btn7.set("")
    btn8.set("")
    btn9.set("")


play()
root.mainloop()
