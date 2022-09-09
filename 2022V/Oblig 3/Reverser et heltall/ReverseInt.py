import tkinter as tk


class Reverseint:
    def __init__(self):

        self.revr_num = 0

        self.main = tk.Tk()
        self.main.title("ReverseInt")
        self.main.resizable(False, False)

        self.wholenumb = tk.IntVar(value="Enter a number.")

        tk.Entry(self.main, width=10, textvariable=self.wholenumb).grid(column=0, row=0, pady=10, padx=5)
        tk.Button(self.main, text="Reverse", command=self.buttonclick).grid(column=1, row=0, pady=10, padx=5)

        self.num_field = tk.Entry(self.main, width=12)
        self.num_field.grid(columnspan=2, column=0, row=1, padx=10, pady=10)

        self.main.mainloop()

    def buttonclick(self):
        try:
            self.num_field.delete(0, "end")
            self.reverseInteger(self.wholenumb.get())
            self.num_field.insert("end", self.revr_num)
            self.revr_num = 0
        except tk.TclError as e:
            self.num_field.insert("end", e)

    def reverseInteger(self, num):
        if num > 0:
            Reminder = num % 10
            self.revr_num = (self.revr_num * 10) + Reminder
            self.reverseInteger(num // 10)


if __name__ == "__main__":
    Reverseint()
