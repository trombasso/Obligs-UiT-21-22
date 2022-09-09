import tkinter as tk
from tkinter import ttk
from random import randint


class Shapes:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Display Shapes")
        self.root.geometry("300x350")
        self.root.resizable(False, False)

        self.selection = tk.StringVar()
        self.select_shape = ttk.Combobox(self.root, textvariable=self.selection, justify="center", width=20)
        self.select_shape["values"] = ["--- Select Shape ---", "Rectangle", "Oval", "Arc", "Polygon", "Line"]
        self.select_shape["state"] = "readonly"
        self.select_shape.current(0)
        self.select_shape.grid(column=0, row=0)
        self.select_shape.bind("<<ComboboxSelected>>", self.shapechange)

        self.shape = tk.Canvas(self.root, width=300, height=320, bg="white")
        self.shape.create_line(0, 0, 0, 0, tag="shapes")
        self.shape.grid(column=0, row=1)

        self.root.mainloop()

    def shapechange(self, *args):
        x = 10
        y = 290
        self.shape.delete("shapes")
        if self.select_shape.get() == "Rectangle":
            # self.shape = tk.Canvas(self.root)
            self.shape.create_rectangle(x, x, y, y, outline="#000000", fill=None, tag="shapes")
            # self.shape.grid(column=0, row=1)
        elif self.select_shape.get() == "Oval":
            # self.shape = tk.Canvas(self.root)
            self.shape.create_oval(10, 10, 285, 160, outline="#000000", fill="red", tag="shapes")
            # self.shape.grid(column=0, row=1)
        elif self.select_shape.get() == "Arc":
            # self.shape = tk.Canvas(self.root)
            self.shape.create_arc(10, 10, 285, 160, outline="#000000", fill="red", width=3, tag="shapes")
            # self.shape.grid(column=0, row=1)
        elif self.select_shape.get() == "Polygon":
            coords = [
                randint(x, y),
                randint(x, y),
                randint(x, y),
                randint(x, y),
                randint(x, y),
                randint(x, y),
                randint(x, y),
                randint(x, y),
                randint(x, y),
                randint(x, y),
                randint(x, y),
                randint(x, y),
            ]
            # self.shape = tk.Canvas(self.root)
            self.shape.create_polygon(coords, outline="#000000", fill="red", width=3, tag="shapes")
            # self.shape.grid(column=0, row=1)
        elif self.select_shape.get() == "Line":
            # self.shape = tk.Canvas(self.root)
            self.shape.create_line(0, 0, 300, 320, fill="red", width=3, tag="shapes")
            # self.shape.grid(column=0, row=1)
        # else:
        #     self.shape = tk.Canvas(self.root)
        #     self.shape.grid(column=0, row=1)


if __name__ == "__main__":
    Shapes()
