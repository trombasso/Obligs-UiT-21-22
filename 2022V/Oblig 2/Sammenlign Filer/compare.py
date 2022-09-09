import os

FILE_PATH = os.path.dirname(__file__)


# Lager liste med unike ord, fjerner duplikater
def process_line(line, word_counts):
    line = replace_chars(line)
    word_lst = line.split()
    for word in word_lst:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1


# Fjerner uønskede tegn fra listen
def replace_chars(line):
    for chars in line:
        if chars in '~@#$%^&*()_-+=~"<>?/,.;!{}[]|':
            line = line.replace(chars, " ")
    return line


# Siler ut duplikater fra innlesing og gir ut
# antallet unike ord, samt liste med disse ordene.
def unique_words(file_lst):
    count = 0
    words = []
    for x in file_lst:
        if x[0] == 1:
            count += 1
            words.append(x[1])

    return count, words


# Leser inn fil, kaller inn replaceChars, process_line og unique_words
# Gir ut en dobbel retur med antall unike og liste med ordene.
def readfile(filename):
    file = open(file=os.path.join(FILE_PATH, filename), mode="r")
    word_counts = {}
    for line in file:
        process_line(line.lower(), word_counts)
    file.close()

    word_counts = list(word_counts.items())
    word_counts = [[x, y] for (y, x) in word_counts]
    word_counts.sort()

    count, words = unique_words(word_counts)

    return count, words


# Returnerer felles ord fra begge filer.
def common_words(file1, file2):
    return set(file1) & set(file2)


# Retunerer unike ord fra file
def uniqe_words_single_file(file, compare):
    return set(file) - set(compare)


def main():

    count_unique_file1, words_unique_file1 = readfile("file1.txt")
    count_unique_file2, words_unique_file2 = readfile("file2.txt")

    # Viser antallet unike ord i filene
    print("\nNumber of uniqe words in file 1: ", count_unique_file1)
    print("Number of uniqe words in file 2: ", count_unique_file2)

    # Viser alle unike ord i begge filer
    print("\nUniqe words from file 1:")
    for x in words_unique_file1:
        print(x, end=", ")
    print("\n\nUniqe words from file 2:")
    for x in words_unique_file2:
        print(x, end=", ")

    # Viser alle unike ord som forekommer både i første og andre fil (felles ord)
    commons = common_words(words_unique_file1, words_unique_file2)
    print("\n\nCommon words from both files: ")
    for x in commons:
        print(x, end=", ")

    # Viser alle unike ord som forekommer i første fil, men ikke i andre
    compare_file1 = uniqe_words_single_file(words_unique_file1, words_unique_file2)
    print("\n\nUnique words in file1 but not in file2")
    for x in compare_file1:
        print(x, end=", ")

    # Viser alle unike ord som forekommer i andre fil, men ikke i første
    compare_file2 = uniqe_words_single_file(words_unique_file2, words_unique_file1)
    print("\n\nUnique words in file2 but not in file1")
    for x in compare_file2:
        print(x, end=", ")

    # Viser alle unike ord som forekommer enten i første eller i andre fil, bortsett fra felles ord
    print("\n\nAll unique words from both files that are not common: ")
    for x in compare_file1:
        print(x, end=", ")
    for x in compare_file2:
        print(x, end=", ")


if __name__ == "__main__":
    main()
