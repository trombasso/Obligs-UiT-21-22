def is_sorted(lst):
    user_lst = lst.split()
    lst = lst.split()

    for i in range(0, len(lst)):
        lst[i] = int(lst[i])

    for i in range(0, len(user_lst)):
        user_lst[i] = int(user_lst[i])

    for x in range(len(lst) - 1):
        # Find the minimum in user input
        current_minmum = min(lst[x:])
        current_min_index = x + lst[x:].index(current_minmum)

        # Swap lst[i] with lst[currentMinIndex] if necessary
        if current_min_index != x:
            lst[current_min_index], lst[x] = lst[x], current_minmum

    if user_lst == lst:
        return True
    else:
        return False, lst


def main():
    user_lst = input("Enter a list of numbers seperated by space:\n")
    if is_sorted(user_lst) is True:
        print("The list is already sorted :D Good job!")
    else:
        print(f"You list is a mess! It should look like this: {is_sorted(user_lst)[1]}")


if __name__ == "__main__":
    main()
