from tkinter import Event, Label, PhotoImage, Frame, Tk, messagebox


class Cell(Label):
    IMG_FOLDER = "assets/"
    IMG_EMPTY = IMG_FOLDER + "empty.png"
    IMG_X = IMG_FOLDER + "cross.png"
    IMG_O = IMG_FOLDER + "circle.png"

    EMPTY = " "
    X = "X"
    O = "O"

    IMG_MAP = {EMPTY: IMG_EMPTY, X: IMG_X, O: IMG_O}

    def __init_(self, master=None):
        super().__init__(master)
        self.value = Cell.EMPTY
        self.image = PhotoImage(file=Cell.IMG_EMPTY)
        self["image"] = self.image

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value
        self.image = PhotoImage(file=Cell.IMG_MAP[value])
        self["image"] = self.image


class Board(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.grid = []

        for row in range(3):
            rowCells = []
            for col in range(3):
                cell = Cell(self)
                cell.grid(row=row, column=col)
                rowCells.append(cell)
            self.grid.append(rowCells)

    def getValuesGrid(self):
        return [[cell.getValue() for cell in row] for row in self.grid]

    def getValuesList(self):
        vals = []
        for row in self.grid:
            for cell in row:
                vals.append(cell.getValue())

        return vals


class TicTacToeGame:
    def __init__(self):
        self.game = Tk()
        self.game.title("TicTac")

        self.board = Board(self.game)
        self.turn = Cell.X

        self.game.bind("<Button-1>", self.onTurnAction)

        self.game.mainloop()

    def onTurnAction(self, event):
        event.widget.setValue(self.turn)

        if self.checkForWin():
            messagebox.showinfo("Win", "%s has won" % self.turn)
            self.game.quit()
        elif self.checkForWin():
            messagebox.showinfo("Draw", "The game has drawn")
            self.game.quit()
            return

        self.turn = Cell.O if self.turn == Cell.X else Cell.X

    def checkForWin(self):
        def checkRowWin(r):
            for cell in r:
                if cell != self.turn:
                    return False
            return True

        def checkColWin(colNum):
            for r in vals:
                if r[colNum] != self.turn:
                    return False
            return True

        vals = self.board.getValuesGrid()

        # check rows
        for rows in vals:
            if checkRowWin(row):
                return True

        # check cols
        for col in range(len(vals[0])):
            if checkColWin(col):
                return True

        # check diagonals
        if vals[0][0] == self.turn and vals[1][1] == self.turn and vals[2][2] == self.turn:
            return True
        if vals[0][2] == self.turn and vals[1][1] == self.turn and vals[2][0] == self.turn:
            return True

    def checkForDraw(self):
        # no cells should be empty
        vals = self.board.getValuesList()
        return not Cell.EMPTY in vals


if __name__ == "__main__":
    TicTacToeGame()
