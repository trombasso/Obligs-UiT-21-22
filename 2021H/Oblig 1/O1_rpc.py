import random

win = "You are the winner! :D "
loose = "Looser! :("

userinput = False
while userinput is False:
    number = random.randint(0, 2)
    userinput = input("Rock (0), Paper(1) og Scissors (2)? ")

    if int(userinput) == number:
        print("It's a tie, try again!")
    elif int(userinput) == 0:
        if number == 1:
            print("Computer choose Paper. " + loose)
        if number == 2:
            print("Computer choose Scissors. " + win)
    elif int(userinput) == 1:
        if number == 0:
            print("Computer choose Rock. " + win)
        if number == 2:
            print("Computer choose Scissors. " + loose)
    elif int(userinput) == 2:
        if number == 0:
            print("Computer choose Rock. " + loose)
        if number == 1:
            print("Computer choose Paper. " + win)
    else:
        print("Only 0, 1 or 2. Or press 9 to quit.")

    if int(userinput) == 9:
        print("Quitting Programme...")
        userinput = True
    else:
        userinput = False
