"""
(Game: Tic-tac-toe) Write a program that plays the tic-tac-toe game.
Two players take turns clicking an available cell in a 3×3 grid with 
their respective tokens (either X or O). When one player has placed 
three tokens in a horizontal, vertical, or diagonal row on the grid, 
the game is over and that player has won. A draw (no winner) occurs when 
all the cells in the grid have been filled with tokens and neither player 
has achieved a win.

Assume that all the cells are initially empty and that the first player 
takes the X token and the second player the O token. To mark a cell, the 
player points the mouse to the cell and clicks it. If the cell is empty, 
the token (X or O) is displayed. If the cell is already filled, the 
player's action is ignored.

Define a custom class named Cell that extends Label for displaying a token 
and for responding to the button-click event. The class contains a data 
field token with three possible values—' ', X, and O—that denote whether 
the cell has been occupied and which token is used in the cell if it is occupied.
"""

import tkinter as tk
from tkinter.constants import CENTER


def TicTacToe():
    window = tk.Tk()
    window.title("-   TicTacToe   -")
    window.geometry("304x330")  # Set the size of the window
    window.resizable(False, False)  # Make the window size fixed

    game_frame = tk.Frame(window)
    game_frame.pack()

    # Initiate assets
    empty = tk.PhotoImage(file="assets/empty.png")
    circle = tk.PhotoImage(file="assets/circle.png")
    cross = tk.PhotoImage(file="assets/cross.png")

    cell1 = tk.Label(game_frame, image=empty, bd=0).grid(row=0, column=0)
    cell2 = tk.Label(game_frame, image=empty, bd=0).grid(row=0, column=1)
    cell3 = tk.Label(game_frame, image=empty, bd=0).grid(row=0, column=2)
    cell4 = tk.Label(game_frame, image=empty, bd=0).grid(row=1, column=0)
    cell5 = tk.Label(game_frame, image=empty, bd=0).grid(row=1, column=1)
    cell6 = tk.Label(game_frame, image=empty, bd=0).grid(row=1, column=2)
    cell7 = tk.Label(game_frame, image=empty, bd=0).grid(row=2, column=0)
    cell8 = tk.Label(game_frame, image=empty, bd=0).grid(row=2, column=1)
    cell9 = tk.Label(game_frame, image=empty, bd=0).grid(row=2, column=2)
    text = tk.Label(game_frame, text="Welcome to TicTacToe. Click to start!", justify=CENTER).grid(row=3, column=0, columnspan=3)

    window.bind("<Button-1>", processMouseEvent)

    window.mainloop()


def processMouseEvent(event):
    print("Clicked at", event.widget)
    # if "label5" in event.widget:
    #     print("Hurra")


TicTacToe()
