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

# DIAGONALS
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

row = []
for x in range(len(theboard)):
    row.append(sum(theboard[x]))

column = []
for x in range(len(theboard)):
    column.append(sum(i[x] for i in theboard))

summary_check = []
for x in diagonal1:
    summary_check.append(sum(x))
for x in diagonal2:
    summary_check.append(sum(x))
for x in row:
    summary_check.append(x)
for x in column:
    summary_check.append(x)

for x in summary_check:
    if x > 1:
        print("Bajs")


# print(summary_check)
