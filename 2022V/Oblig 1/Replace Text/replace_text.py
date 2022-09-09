import os


def replace_text(filename, old_string, new_string):
    file_dir = os.path.dirname(__file__)
    with open(file=os.path.join(file_dir, filename)) as file:
        filedata = file.read()
        if old_string in filedata:
            filedata = filedata.replace(old_string, new_string)
            with open(file=os.path.join(file_dir, filename), mode="w") as file:
                file.write(filedata)
        else:
            print("Can not find string in file.")
            exit()


def main():
    filename = input("Enter a filename: ")  # test.txt supplied in repo
    old_string = input("Enter the old string to be replaced: ")
    new_string = input("Enter the new string to replace the old string:")

    try:
        replace_text(filename, old_string, new_string)
    except FileNotFoundError:
        print("File Not Found!")
        exit()


if __name__ == "__main__":
    main()
