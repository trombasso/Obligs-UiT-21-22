class EQ:
    def __init__(self, queens=8 * [-1]):
        self.queens = queens

    def get(self, i):
        return self.queens[i]

    def set(self, i, j):
        self.queens[i] = j

    def is_solved(self):
        """
        is_solved" checks if queens are placed correctly on the board.
        --------------------------------------------------------------
        1) creates a matrix where queens are 1 and empty spaces are 0
        2) Sums the board diagonally, starts in the upper left corner and the upper right corner and
            simultaniously sums in X-pattern to opposite corners.
        3) Sum rows and columns
        4) Collects all sums in a singel list, checking if any elemt of list is above 1.
        5) Returns True if all elements are 1 or below.
        """
        # Creates matrix
        theboard = []
        for elem in range(0, len(self.queens)):
            theboard.append([])
        for x in range(0, 8):
            for y in range(0, 8):
                if self.queens[x] == y:
                    theboard[x].append(1)
                else:
                    theboard[x].append(0)

        # Sums diagonals, first 0 through 8...
        diagonal1 = []
        diagonal2 = []
        x = 1
        for elem in range(0, 8):
            diagonal1.append([])
            a, b = 0, elem
            diagonal2.append([])
            c, d = elem, 7

            for y in range(0, x):
                diagonal1[len(diagonal1) - 1].append(theboard[a][b])
                a += 1
                b -= 1
                diagonal2[len(diagonal2) - 1].append(theboard[c][d])
                d -= 1
                c -= 1
            x += 1

        # ...then 7 through 15.
        x -= 2
        for elem in range(0, 7):
            diagonal1.append([])
            a, b = elem + 1, 7
            diagonal2.append([])
            c, d = 7, 6 - elem

            for y in range(0, x):
                diagonal1[len(diagonal1) - 1].append(theboard[a][b])
                b -= 1
                a += 1
                diagonal2[len(diagonal2) - 1].append(theboard[c][d])
                c -= 1
                d -= 1
            x -= 1

        # Sums up rows and columns.
        row = []
        for x in range(len(theboard)):
            row.append(sum(theboard[x]))
        column = []
        for x in range(len(theboard)):
            column.append(sum(i[x] for i in theboard))

        # for testing
        # for elem in diagonal1:
        #     print(elem)
        # for elem in diagonal2:
        #     print(elem)
        # for elem in row:
        #     print(elem)
        # for elem in column:
        #     print(elem)

        # Collects all sums to a list.
        summary_check = []
        for x in diagonal1:
            summary_check.append(sum(x))
        for x in diagonal2:
            summary_check.append(sum(x))
        for x in row:
            summary_check.append(x)
        for x in column:
            summary_check.append(x)

        # Last check. Return True if no Queen can get to another.
        for x in summary_check:
            if x > 1:
                return False
        return True

    def print_board(self):
        for x in range(0, 8):
            for y in range(0, 8):
                if self.queens[x] == y:
                    print("|Q", end="")
                else:
                    print("| ", end="")
            print("|", end="\n")


def main():
    # Assigment code...
    board1 = EQ()
    board1.set(0, 2)
    board1.set(1, 4)
    board1.set(2, 7)
    board1.set(3, 1)
    board1.set(4, 0)
    board1.set(5, 3)
    board1.set(6, 6)
    board1.set(7, 5)

    print("Is board1 a correct eight queen placement?", board1.is_solved())

    board2 = EQ([0, 4, 7, 5, 2, 6, 1, 3])

    if board2.is_solved():
        print("Eight queens are placed correctly in board2")
        board2.print_board()
    else:
        print("Eight queens are placed incorrectly in board2")


if __name__ == "__main__":
    main()
