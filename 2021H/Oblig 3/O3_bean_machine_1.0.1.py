import random
from os import name, system


def clear():
    if name == "nt":  # for windows
        _ = system("cls")
    else:  # for mac and linux
        _ = system("clear")


# Handles calculations of ball trajectories and what slot they end up in.
def bean_machine(balls, slots):
    ball_directions = {}
    slot_list = []

    # creates slot lists
    for x in range(0, slots):
        slot_list.append(0)

    # create dictionarys and fill with random LR's for each ball
    for x in range(1, balls + 1):
        ball_directions[x] = []
        counting_r = 0

        for y in range(0, slots - 1):
            i = random.randint(0, 1)
            if i == 0:  # left
                ball_directions[x].append("L")
            if i == 1:  # right
                ball_directions[x].append("R")

    # count number og R´s in dictionary for each key and add to countlist
    for x in range(1, len(ball_directions) + 1):
        counting_r = 0
        for i in range(0, len(ball_directions[x])):
            if ball_directions[x][i] == "R":
                counting_r += 1
            else:
                pass
        slot_list[counting_r] += 1

    # print(ball_directions, slot_list)
    return ball_directions, slot_list


# Handles all printing to screen
def bean_machine_print(ball_directions, slot_list):
    slots = len(slot_list)
    compare = max(slot_list)
    placement = 0

    # Prints ball_directions at top of screen
    print("\nBall Directions: \n")
    for i in ball_directions:
        for a in range(0, len(ball_directions[i])):
            print(ball_directions[i][a], end="")
        print(",", end="")
    print("\n\n")

    # Graphics section, prints
    for i in range(0, slots * max(slot_list)):
        if placement == 0:
            print("|", end="")
        if slot_list[placement] < compare:
            print("     ", end="")
        if slot_list[placement] >= compare:
            print("    ", end="")

        if placement == slots - 1:
            print("|", end="\n")
            placement = 0
            compare -= 1
        else:
            placement += 1

    for i in range(0, slots):
        print("-----", end="")
    print("--\n| ", end="")
    for i in slot_list:
        print("", "{0:>2}".format(i), end=" |")
    print("\n")


def main():
    clear()
    while True:
        try:
            balls = int(input("Enter the number of balls to drop: "))
            slots = int(input("Enter the number of slots: "))
            break
        except Exception:
            print("...eh, enter a number!\n")

    clear()
    loop = True
    while loop:
        bean_machine_output = bean_machine(balls, slots)
        slot_list = bean_machine_output[1]
        ball_directions = bean_machine_output[0]
        bean_machine_print(ball_directions, slot_list)
        ask_if_loop = input("Repeat trial? ( Y/N ) ").upper()
        if ask_if_loop == "N":
            break
        else:
            clear()
            continue
    exit()


if __name__ == "__main__":
    main()
