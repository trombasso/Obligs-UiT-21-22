from os import name, system
import O5_Account_class as ac
from time import sleep


# Clearing the screen
def clear():
    if name == "nt":  # for windows
        _ = system("cls")
    else:  # for mac and linux
        _ = system("clear")


def main_menu(value):
    while True:
        try:
            clear()
            print("---------------- ATM ----------------\n")
            print("1: withdraw")
            print("2: deposit")
            print("3: exit\n\n\n")
            print(f"Current account balance: ${value}")
            print("-------------------------------------\n")
            print("Enter a choice: ", end="")
            choice = int(input())
            if choice < 1 or choice > 3:
                raise ValueError
            else:
                return choice
        except ValueError:
            print("Unvalid entry, try again!")
            sleep(2)


def login():
    while True:
        try:
            clear()
            print("---------------- ATM ----------------\n\n")
            print("               Welcome!\n")
            print("            Login to your")
            print("               account")
            print("\n")
            print("-------------------------------------\n")
            id = int(input("Enter ID: "))
            if id == 1234:
                exit()
            break
        except ValueError:
            print("Not a valid account number.\nPlease try again! ")
            sleep(2)
    return id


def create_accounts():
    accounts = []
    for i in range(10):
        accounts.append(ac.Account(i, 100))
    return accounts


def main():
    accounts = create_accounts()

    atm_running = True
    while atm_running is True:

        loop = True
        while loop:
            id = login()
            for elem in range(len(accounts)):
                if id == accounts[elem].id:
                    loop = False
                    logged_in = True
                    break
            else:
                print("\n Account does not exist!")
                sleep(2)

        while logged_in is True:
            menu_choice = main_menu(accounts[id].balance)
            if menu_choice is 1:
                withdraw_amount = float(input("Enter amount:"))
                if accounts[id].balance >= withdraw_amount:
                    accounts[id].withdraw(withdraw_amount)
                else:
                    print("\nNo sufficient funding.")
                    sleep(2)
            elif menu_choice is 2:
                accounts[id].deposit(float(input("Enter amount: ")))
            elif menu_choice is 3:
                logged_in = False


if __name__ == "__main__":
    main()
