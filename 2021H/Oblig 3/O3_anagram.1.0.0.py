# Check if s1 and s2 are anagrams
def is_anagram(s1, s2):
    s1 = list(s1)
    s2 = list(s2)

    # Converting s1 to ord() and sorting ints in list.
    for i in range(0, len(s1)):
        s1[i] = ord(s1[i])

    for x in range(len(s1) - 1):
        current_min = min(s1[x:])
        current_min_index = x + s1[x:].index(current_min)

        if current_min_index != x:
            s1[current_min_index], s1[x] = s1[x], current_min

    # Converting s2 to ord() and sorting ints in list.
    for i in range(0, len(s2)):
        s2[i] = ord(s2[i])

    for x in range(len(s2) - 1):
        current_min = min(s2[x:])
        current_min_index = x + s2[x:].index(current_min)

        if current_min_index != x:
            s2[current_min_index], s2[x] = s2[x], current_min

    # Comparing s1 and s2.
    if s1 == s2:
        return True
    else:
        return False


def main():
    s1 = input("Enter the first string: ").lower()
    s2 = input("Enter the second string: ").lower()
    if is_anagram(s1, s2) is True:
        print(f"{s1} and {s1} are anagrams.")
    else:
        print(f"{s1} and {s2} are not anagrams.")


if __name__ == "__main__":
    main()
