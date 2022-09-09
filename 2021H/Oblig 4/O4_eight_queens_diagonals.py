theboard = [
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
]

diagonal1 = []
diagonal2 = []

# DIAGONAL
x = 1
for elem in range(0, 8):
    diagonal1.append([])
    a, b = 0, elem
    for y in range(0, x):
        # print(theboard[a][b], end="")
        diagonal1[len(diagonal1) - 1].append(theboard[a][b])
        a += 1
        b -= 1
    x += 1
    # print("\n")

x -= 2
for elem in range(0, 7):
    diagonal1.append([])
    a, b = elem + 1, 7
    for y in range(0, x):
        # print(theboard[a][b], end="")
        diagonal1[len(diagonal1) - 1].append(theboard[a][b])
        b -= 1
        a += 1
    x -= 1
    # print("\n")


# OPOSITE DIAGONAL
x = 1
for elem in range(0, 8):
    diagonal2.append([])
    a, b = elem, 7
    for y in range(0, x):
        # print(theboard[a][b], end="")
        diagonal2[len(diagonal2) - 1].append(theboard[a][b])
        a -= 1
        b -= 1
    x += 1
    # print("\n")


x -= 2
for elem in range(0, 7):
    diagonal2.append([])
    a, b = 7, 6 - elem
    for y in range(0, x):
        # print(theboard[a][b], end="")
        diagonal2[len(diagonal2) - 1].append(theboard[a][b])
        a -= 1
        b -= 1
    x -= 1

    # print("\n")

for x in diagonal1:
    print(sum(x))

for x in diagonal2:
    print(sum(x))
