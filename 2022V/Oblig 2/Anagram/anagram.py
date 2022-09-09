def is_anagram(word_1, word_2):
    d = {}
    for letters in word_1, word_2:
        d[letters] = {}
        for c in letters:
            d[letters][c] = d[letters].get(c, 0) + 1
    return d[word_1] == d[word_2]


def main():
    word_1 = input("Please enter first word: ").lower()
    word_2 = input("Please enter second word: ").lower()

    print(f"The words {'are' if is_anagram(word_1, word_2) else 'are not'} anagrams.")


if __name__ == "__main__":
    main()
