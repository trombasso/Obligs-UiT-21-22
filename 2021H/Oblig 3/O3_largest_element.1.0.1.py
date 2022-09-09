def locate_largest(lst1):
    lst2 = []
    # Appends the index of the row containing the highest number
    lst2.append(list(map(max, lst1)).index(max(list(map(max, lst1)))))
    # Appends the index of highest number in row.
    lst2.append(lst1[lst2[0]].index(max(lst1[lst2[0]])))
    largest_elem = lst1[lst2[0]][lst2[1]]
    return lst2, largest_elem


def main():
    lst1, lst2 = [], []
    rows = int(input("How many rows: "))

    for i in range(rows):
        insert = input("Enter a row:")

        # Convert input to a float list and append to lst1
        insert = [int(x) for x in insert.split()]
        lst1.append(insert)

    lst2, largest_elem = locate_largest(lst1)

    print(f"\nThe location of the largest element is at ({lst2[0]},{lst2[1]})\n\nThe number is {largest_elem}.")


if __name__ == "__main__":
    main()
