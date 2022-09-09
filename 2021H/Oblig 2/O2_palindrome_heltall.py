# Return the reversal of an integer, e.g. reverse(456) returns 654
def reverse(number):
    input_list_reversed = []
    for x in range(1, len(number) + 1):
        input_list_reversed.append(number[len(number) - x])

    reverse_number = ""
    return reverse_number.join(input_list_reversed)


# Return true if number is a palindrome
def is_palindrome(user_input):
    input_list = list(user_input)
    input_list_reversed = reverse(input_list)
    if input_list_reversed == user_input:
        return True
    else:
        return False


def main():
    print("\nPalindromechecker 2.1")
    while True:
        try:
            user_input = int(input("Enter integers to check for palindrome: "))
        except (ValueError):
            print("Input not recognized as integers, try again.")
            continue
        else:
            break

    if is_palindrome(str(user_input)) is True:
        print(f"\nYes, <{user_input}> is a palindrome!\n")
    else:
        print(f"\nSorry, <{user_input}> is not a palindrome.\n")


if __name__ == "__main__":
    main()
