import tkinter as tk

PAD_X = 10
PAD_Y = 5


class GUI:
    def __init__(self):
        win = tk.Tk()
        win.title("Bitwise Operators")
        win.geometry("850x150")
        win.resizable(False, False)

        tk.Label(win, text="First number, range 0-255").grid(column=0, row=0, sticky=(tk.E), padx=PAD_X, pady=PAD_Y)
        tk.Label(win, text="Second number, range 0-255").grid(column=0, row=1, sticky=(tk.E), padx=PAD_X, pady=PAD_Y)
        tk.Label(win, text="Your answer").grid(
            column=0,
            row=2,
            sticky=(tk.E),
            padx=PAD_X,
            pady=PAD_Y,
        )
        tk.Label(win, text="Correct answer").grid(column=0, row=3, sticky=(tk.E), padx=PAD_X, pady=PAD_Y)

        self.input_a = tk.IntVar(win)
        tk.Entry(win, textvariable=self.input_a, width=4, background="Black").grid(column=1, row=0)

        self.input_b = tk.IntVar(win)
        tk.Entry(win, textvariable=self.input_b, width=4, background="Black").grid(column=1, row=1)

        self.bits_input_a = tk.IntVar()
        tk.Label(win, textvariable=self.bits_input_a, width=10).grid(column=2, row=0)

        self.bits_input_b = tk.IntVar()
        tk.Label(win, textvariable=self.bits_input_b, width=10).grid(column=2, row=1)

        self.input_c = tk.IntVar()
        self.entryfield = tk.Entry(win, width=8, textvariable=self.input_c, background="Black")
        self.entryfield.grid(column=2, row=2)

        self.bits_answer = tk.IntVar()
        tk.Label(win, textvariable=self.bits_answer, width=10).grid(column=2, row=3)

        tk.Label(win, text="Only this for SHIFTRIGHT(1), SHIFTLEFT(1), OCOMP").grid(column=3, row=0, sticky=(tk.W), padx=PAD_X, pady=PAD_Y)

        OPTIONS = ["AND", "OR", "OCOMP", "XOR", "SHIFTLEFT", "SHIFTRIGHT"]

        self.operator = tk.StringVar(win)
        self.operator.set(OPTIONS[0])  # default value

        self.operator_menu = tk.OptionMenu(win, self.operator, *OPTIONS).grid(column=3, row=2)
        tk.Button(win, text="CHECK!", command=self.check).grid(column=4, row=0, rowspan=4)

        win.bind_class("Entry", "<FocusOut>", self.on_focus_out)

        win.mainloop()

    def on_focus_out(self, event):
        try:
            self.bits_input_a.set(self.convertIntToBin(self.input_a.get()))
        except Exception:
            self.bits_input_a.set("ERROR!")
        try:
            self.bits_input_b.set(self.convertIntToBin(self.input_b.get()))
        except Exception:
            self.bits_input_b.set("ERROR!")
        self.entryfield.configure({"background": "Black"})

    def check(self):
        try:
            operator = self.operator.get()
            a = self.input_a.get()
            b = self.input_b.get()
        except Exception:
            self.bits_answer.set("ERROR!")

        try:
            if operator == "AND":
                self.bits_answer.set(self.convertIntToBin(a & b))
            elif operator == "OR":
                self.bits_answer.set(self.convertIntToBin(a | b))
            elif operator == "OCOMP":
                self.bits_answer.set(self.convertIntToBin(~a & 255))
            elif operator == "XOR":
                self.bits_answer.set(self.convertIntToBin(a ^ b))
            elif operator == "SHIFTLEFT":
                self.bits_answer.set(self.convertIntToBin(a << 1))
            elif operator == "SHIFTRIGHT":
                self.bits_answer.set(self.convertIntToBin(a >> 1))

            if self.input_c.get() == self.bits_answer.get():
                self.entryfield.configure({"background": "green"})
            else:
                self.entryfield.configure({"background": "red"})

        except Exception:
            self.bits_answer.set("ERROR!")

    def convertIntToBin(self, number):
        # return f"{number:>08b}"
        # return f"{number:>8b}"
        return bin(number).replace("0b", "")


def main():
    GUI()


if __name__ == "__main__":
    main()
