import random
from os import name, system


# Clearing the screen
def clear():
    if name == "nt":  # for windows
        _ = system("cls")
    else:  # for mac and linux
        _ = system("clear")


def bean_machine(balls, slots):
    loop = True
    while loop:
        ball_directions = {}
        slot_list = []

        # create slot list
        for x in range(0, slots):
            slot_list.append(0)

        # create dictionary and fill with random LR's
        for x in range(1, balls + 1):
            ball_directions[x] = []
            counting_r = 0

            # generate random LR's for ball
            for y in range(0, slots - 1):
                i = random.randint(0, 1)
                if i == 0:  # left
                    ball_directions[x].append("L")
                if i == 1:  # right
                    ball_directions[x].append("R")

        # count R´s in dictionary for each key and add to countlist
        for x in range(1, len(ball_directions) + 1):
            counting_r = 0
            for i in range(0, len(ball_directions[x])):
                if ball_directions[x][i] == "R":
                    counting_r += 1
                else:
                    pass
            slot_list[counting_r] += 1

        # print(ball_directions)
        print("\nBall Directions: \n")
        for i in ball_directions:
            for a in range(0, len(ball_directions[i])):
                print(ball_directions[i][a], end="")
            print(",", end="")
        print("\n\n")

        # print graphics with balls
        compare = max(slot_list)
        placement = 0
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

        # Ask to repeat with same input.
        ask_if_loop = input("Repeat trial? ( Y/N ) ").upper()
        if ask_if_loop == "N":
            break
        else:
            clear()
            continue


def main():
    clear()
    while True:
        try:
            balls = int(input("Enter the number of balls to drop: "))
            slots = int(input("Enter the number of slots: "))
            break
        except ValueError:
            print("...eh, enter a number!\n")
    bean_machine(balls, slots)


if __name__ == "__main__":
    main()
