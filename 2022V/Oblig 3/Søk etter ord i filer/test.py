import os

"""
/Users/anderskarlskas/Dropbox/Dokumenter/Programmering/Grunnleggende Programmering/Obligatoriske/2022V/Oblig 3/Søk etter ord i filer/mappe1
/Users/anderskarlskas/Dropbox/Dokumenter/Programmering/Grunnleggende Programmering/Obligatoriske/2022V/Oblig 3/Søk etter ord i filer
"""

word_lst = []


def find_word(dir, phrase):
    try:
        dir_lst = [i for i in os.listdir(dir) if i[0] != "."]
        for file in dir_lst:
            path = dir + "/" + file
            if os.path.isdir(path):
                # Rekursiv metode for å dykke inn i underkatalog
                find_word(path, phrase)
            else:
                with open(file=path, mode="r") as file:
                    for line in file.readlines():
                        if phrase in line:
                            word_lst.append([path, ":   ", line.strip()])
    except FileNotFoundError:
        return "Folder does not exist"
    return word_lst


dir = input("Enter directory/filename: ")
phrase = input("Word: ")
lst = find_word(dir, phrase)
for i in lst:
    print(i, end="\n")
