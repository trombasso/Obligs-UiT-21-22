from os import system, name
from time import sleep


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


clear()
print()
print("BMI Calculator")
print("-----------------------------")
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))
bmi = weight / height ** 2
print("-----------------------------")
print(f"Your BMI is: {bmi:.2f}")
print()
sleep(5)
clear()
