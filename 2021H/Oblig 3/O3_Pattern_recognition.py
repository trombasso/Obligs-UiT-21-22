def is_consecutive_four(values):
    values_lst = [int(x) for x in values.split()]
    for i in range(0, len(values_lst) - 3):
        if (
            values_lst[i] == values_lst[i + 1]
            and values_lst[i] == values_lst[i + 2]
            and values_lst[i] == values_lst[i + 3]
        ):
            return True


def main():
    values = input("Enter integers separated by spaces from one line: ")
    if is_consecutive_four(values) is True:
        print("The series has consecutive fours.")
    else:
        print("The series does not contain consecutive fours.")


if __name__ == "__main__":
    main()
