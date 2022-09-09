counter = 0


def main(n):
    # n = int(input("Enter number of disks: "))

    # Find the solution recursively
    print("The moves are:")
    moveDisks(n, "A", "B", "C")


# The function for finding the solution to move n disks
#   from fromTower to toTower with auxTower
def moveDisks(n, fromTower, toTower, auxTower):
    global counter
    if n == 1:  # Stopping condition
        print("Move disk", n, "from", fromTower, "to", toTower)
        counter += 1
    else:
        counter += 1
        moveDisks(n - 1, fromTower, auxTower, toTower)
        print("Move disk", n, "from", fromTower, "to", toTower)
        moveDisks(n - 1, auxTower, toTower, fromTower)


main(5)  # Call the main function
print(counter)
