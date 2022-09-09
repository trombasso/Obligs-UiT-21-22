import tkinter as tk


class Buttons_and_radios:
    def __init__(self):
        # Setting up master window
        root = tk.Tk()
        root.title("Buttons and Radios'n stuff")
        root.geometry("400x145")
        root.resizable(False, False)

        radiobuttons = tk.Frame(root, width=400)
        radiobuttons.pack()
        self.var = tk.StringVar()
        b1 = tk.Radiobutton(radiobuttons, variable=self.var, command=self.process_radio_button, value="R", text="Red")
        b2 = tk.Radiobutton(radiobuttons, variable=self.var, command=self.process_radio_button, value="B", text="Blue")
        b3 = tk.Radiobutton(radiobuttons, variable=self.var, command=self.process_radio_button, value="G", text="Green")
        b4 = tk.Radiobutton(radiobuttons, variable=self.var, command=self.process_radio_button, value="Y", text="Yellow")
        b1.grid(column=0, row=0)
        b2.grid(column=1, row=0)
        b3.grid(column=2, row=0)
        b4.grid(column=3, row=0)

        self.textarea = tk.Canvas(root, width=400, height=80, bg="black")
        self.greeting = self.textarea.create_text(100, 20, text="Lets begin!", fill="white")
        self.textarea.move(self.greeting, 100, 20)
        self.textarea.pack()

        self.naviarea = tk.Frame(root)
        self.naviarea.pack()
        tk.Button(self.naviarea, text="<<", command=self.move_left).grid(column=0, row=0)
        tk.Button(self.naviarea, text=">>", command=self.move_right).grid(column=1, row=0)

        root.bind("<KeyPress-Left>", self.move_left)
        root.bind("<KeyPress-Right>", self.move_right)

        root.mainloop()

    def process_radio_button(self):
        if self.var.get() == "R":
            self.textarea["bg"] = "red"
            self.textarea.itemconfig(self.greeting, text="Red", fill="white")
        elif self.var.get() == "B":
            self.textarea["bg"] = "blue"
            self.textarea.itemconfig(self.greeting, text="Blue", fill="white")
        elif self.var.get() == "G":
            self.textarea["bg"] = "green"
            self.textarea.itemconfig(self.greeting, text="Green", fill="white")
        elif self.var.get() == "Y":
            self.textarea["bg"] = "yellow"
            self.textarea.itemconfig(self.greeting, text="Yellow", fill="black")

    def move_left(self, *args):
        (xpos, ypos) = self.textarea.coords(self.greeting)
        if xpos > 20:
            self.textarea.move(self.greeting, -4, 0)

    def move_right(self, *args):
        (xpos, ypos) = self.textarea.coords(self.greeting)
        if xpos < 380:
            self.textarea.move(self.greeting, +4, 0)


if __name__ == "__main__":
    Buttons_and_radios()
