import tkinter as tk
import os


class FindWordInFile:
    # Main GUI window
    def __init__(self):

        self.folders_num = 0
        self.files_num = 0
        self.phrase_num = 0
        self.folder_not_exist = 0

        self.main = tk.Tk()
        self.main.title("Search for word in files...")
        self.main.resizable(False, False)

        self.dir_name = tk.StringVar(value="Directory or Filename")
        self.phrase = tk.StringVar(value="Word")

        tk.Entry(self.main, width=60, textvariable=self.dir_name).grid(column=0, row=0)
        tk.Entry(self.main, width=20, textvariable=self.phrase).grid(column=1, row=0)

        tk.Button(self.main, text="Search", command=self.buttonclick).grid(column=2, row=0)

        self.text_field = tk.Text(self.main, height=40, width=150)
        self.text_field.grid(columnspan=3, column=0, row=1)

        self.main.mainloop()

    # Hjelpefunksjon for tk.button
    def buttonclick(self):
        self.text_field.insert("end", f"Search start...\n--------------------------------------------------\n\n")
        if self.phrase.get() == "":
            self.text_field.insert("end", "You have to enter a word o.O\n\n")
        else:
            self.find_word(self.dir_name.get(), self.phrase.get())
            self.print_func()

    # Rekursiv metode for å dykke inn i underkatalog
    def find_word(self, dir, phrase):
        try:
            dir_lst = [i for i in os.listdir(dir) if i[0] != "."]
            for file in dir_lst:
                path = dir + "/" + file  #
                if os.path.isdir(path):
                    self.folders_num += 1
                    self.find_word(path, phrase)  # Her går den rekursivt ved katalog
                else:
                    self.files_num += 1
                    with open(file=path, mode="r") as file:
                        for line in file.readlines():
                            if phrase in line:
                                self.phrase_num += 1
                                temp = f"{path}: {line.strip()}\n"
                                self.text_field.insert("end", temp)

        except FileNotFoundError:
            self.folder_not_exist += 1
            return None

    # Printing til "konsollen" i GUI
    def print_func(self):
        if self.folder_not_exist == 1:
            self.text_field.insert("end", "Folder does not exist.\n\n")
            self.folder_not_exist = 0
        elif self.phrase_num == 0:
            self.text_field.insert("end", f"{self.phrase.get()} could not be found!\n\n")
            self.folders_num = 0
            self.files_num = 0
            self.phrase_num = 0
        else:
            self.text_field.insert("end", "--------------------------------------------------\n")
            self.text_field.insert(
                "end",
                f"Searched: {self.folders_num} directories | {self.files_num} files | Found {self.phrase_num} occurences of {self.phrase.get()}\n\n",
            )

            self.folders_num = 0
            self.files_num = 0
            self.phrase_num = 0

            return None


if __name__ == "__main__":
    FindWordInFile()
