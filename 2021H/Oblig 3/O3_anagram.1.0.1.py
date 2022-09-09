# Converts string to list and Ascii ints, sorts into ascending order.
def string_to_sorted_ordlist(string):
    string = list(string)
    for i in range(0, len(string)):
        string[i] = ord(string[i])

    for x in range(len(string) - 1):
        current_min = min(string[x:])
        current_min_index = x + string[x:].index(current_min)

        if current_min_index != x:
            string[current_min_index], string[x] = string[x], current_min
    return string


# Check if s1 and s2 are anagrams
def is_anagram(s1, s2):
    global lst1, lst2
    lst1 = string_to_sorted_ordlist(s1)
    lst2 = string_to_sorted_ordlist(s2)
    if lst1 == lst2:
        return True


def main():
    s1 = input("\nEnter the first string: ").lower()
    s2 = input("Enter the second string: ").lower()
    if is_anagram(s1, s2) is True:
        print(f"\n{s1} and {s1} are anagrams.\n")
    else:
        print(f"\n{s1} and {s2} are not anagrams.\n")


if __name__ == "__main__":
    main()
