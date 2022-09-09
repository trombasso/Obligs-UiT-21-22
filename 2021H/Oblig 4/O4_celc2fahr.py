import tkinter as tk


def calculate(*args):
    try:
        value = float(celcius.get())
        fahrenheit.set(int(value * 1.8 + 32))
    except ValueError:
        pass


root = tk.Tk()
root.title("Celcius to Fahrenheit")
root.geometry(
    "300x120",
)
root.resizable(False, False)

mainframe = tk.Frame(root, width=400, height=150)
mainframe.pack()

celcius = tk.StringVar(mainframe, value="Celcius?")
celcius_entry = tk.Entry(mainframe, width=10, textvariable=celcius)
celcius_entry.grid(column=0, row=2, columnspan=3, pady=10)

fahrenheit = tk.StringVar(value="X")

tk.Button(mainframe, text="Calculate", command=calculate).grid(column=0, row=3, columnspan=3)
tk.Label(mainframe, text="Is").grid(column=0, row=4)
tk.Label(mainframe, textvariable=fahrenheit).grid(column=1, row=4)
tk.Label(mainframe, text="degrees fahrenheit.").grid(column=2, row=4)

celcius_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
