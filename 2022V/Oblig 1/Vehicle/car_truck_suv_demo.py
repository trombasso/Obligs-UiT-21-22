# This program creates a Car object, a Truck object,
# and an SUV object.
from vehicle_errors import LengthError, ModelError, MilageError, DoorError, DriveTypeError, PassCapError
from operator import attrgetter
import vehicles
import os
from os import name, system
from time import sleep
import pickle


# Constants for the menu choices
NEW_CAR_CHOICE = 1
NEW_TRUCK_CHOICE = 2
NEW_SUV_CHOICE = 3
FIND_VEHICLE_CHOICE = 4
SHOW_VEHICLES_CHOICE = 5
QUIT_CHOICE = 6


def clear():
    if name == "nt":  # for windows
        _ = system("cls")
    else:  # for mac and linux
        _ = system("clear")


# The display_menu function displays a menu.
def display_menu():
    clear()
    horisontal_line("menu")
    print("1) New car")
    print("2) New truck")
    print("3) New SUV")
    print("4) Find vehicles by make")
    print("5) Show all vehicles")
    print("6) Quit")
    horisontal_line("line")


def horisontal_line(section):
    if section == NEW_CAR_CHOICE or section == NEW_TRUCK_CHOICE or section == NEW_SUV_CHOICE:
        print("\n----------------------------------- Add new vehicle ----------------------------------\n")
    elif section == FIND_VEHICLE_CHOICE:
        print("\n--------------------------------------- Search ---------------------------------------\n")
    elif section == SHOW_VEHICLES_CHOICE:
        print("\n-------------------------------------- Car List --------------------------------------\n")
    elif section == "menu":
        print("\n---------------------------------------- Menu ----------------------------------------\n")
    elif section == "line":
        print("\n--------------------------------------------------------------------------------------\n")


def read_inventory():
    vehicles_list = []
    file_dir = os.path.dirname(__file__)
    try:
        with open(file=os.path.join(file_dir, "vehicles.dat"), mode="rb") as file:
            vehicles_list = pickle.load(file)
            return vehicles_list
    except FileNotFoundError:
        print("Error!")
        print("Could not find file")
        newfile = input("Would you like create new database? [Y/N]").upper()
        if newfile == "N":
            print("Exiting....")
            exit()
        else:
            return vehicles_list


def save_inventory(vehicles_list):
    print("\nSaving to disk...")
    vehicles_list = sorted(vehicles_list, key=attrgetter("make"))

    file_dir = os.path.dirname(__file__)
    with open(file=os.path.join(file_dir, "vehicles.dat"), mode="wb") as file:
        pickle.dump(vehicles_list, file)
    sleep(1)


def main():
    vehicles_list = read_inventory()

    choice = 0
    while choice != QUIT_CHOICE:
        # display the menu.
        choice = 0  # resetting menu after each pass.
        display_menu()

        # Get the user's choice.
        try:
            choice = int(input("Enter menu choice: "))
            if choice < 1 or choice > 6:
                raise ValueError
        except ValueError as e:
            print("\nError: Velg menyvalg 1-6 (", e, ")")
            sleep(3)

        if choice == NEW_CAR_CHOICE or choice == NEW_TRUCK_CHOICE or choice == NEW_SUV_CHOICE:
            loop = True
            while loop:
                try:
                    make = input("Make: ")
                    if len(make) < 15:
                        break
                    else:
                        raise LengthError
                except LengthError as e:
                    print(e)

            while loop:
                try:
                    model = int(input("Year: "))
                    if model >= 1900 and model <= 2022:
                        break
                    else:
                        raise ModelError
                except ModelError as e:
                    print(e)
                except ValueError as e:
                    print("Error:", e)

            while loop:
                try:
                    milage = int(input("Milage: "))
                    if milage > 0:
                        break
                    else:
                        raise MilageError
                except MilageError as e:
                    print(e)
                except ValueError as e:
                    print("Error:", e)

            while loop:
                try:
                    price = int(input("Price: "))
                    break
                except ValueError as e:
                    print("Error:", e)

            if choice == NEW_CAR_CHOICE:
                while loop:
                    try:
                        doors = int(input("Doors: "))
                        if doors >= 2 and doors <= 4:
                            break
                        else:
                            raise DoorError
                    except DoorError as e:
                        print(e)
                    except ValueError as e:
                        print("Error: ", e)
                vehicles_list.append(vehicles.Car(make, model, milage, price, doors))

            elif choice == NEW_TRUCK_CHOICE:
                while loop:
                    try:
                        drive_type = input("Drive Type: ")
                        if drive_type == "2WD" or drive_type == "4WD":
                            break
                        else:
                            raise DriveTypeError
                    except DriveTypeError as e:
                        print(e)
                vehicles_list.append(vehicles.Car(make, model, milage, price, drive_type))

            elif choice == NEW_SUV_CHOICE:
                while loop:
                    try:
                        pass_cap = input("Passenger Cap: ")
                        if pass_cap > 1:
                            break
                        else:
                            raise PassCapError
                    except PassCapError as e:
                        print(e)
                    except ValueError as e:
                        print("Error", e)
                vehicles_list.append(vehicles.Car(make, model, milage, price, pass_cap))

            horisontal_line("line")
            print("Vehicle added to inventory.\n")
            sleep(1)

        elif choice == FIND_VEHICLE_CHOICE:
            clear()
            horisontal_line(choice)
            name = input("Enter name of vehicle: ")
            search_list = []
            print(f"\nSearchresults for '{name}':\n\n")
            for item in vehicles_list:
                if name in item.get_make():
                    search_list.append(item)
            if search_list == []:
                print("No vehicle found!")
                print("NB! The search is case-sensitive.")
            else:
                for item in search_list:
                    print(item)
            horisontal_line("line")
            input("Press enter to continue...")
            clear()

        elif choice == SHOW_VEHICLES_CHOICE:
            # show all vehicles
            clear()
            horisontal_line(choice)
            for item in vehicles_list:
                print(item)
            horisontal_line("line")
            input("Press enter to continue...")
            clear()
        elif choice == QUIT_CHOICE:
            clear()
            save_inventory(vehicles_list)
            print("\nExiting the program, have a wonderfull day!\n")
        else:
            pass


# Call the main function.
if __name__ == "__main__":
    main()
