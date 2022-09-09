from calendar import monthrange
import datetime


def check_user_input(input):
    try:
        input = int(input)
        return True
    except ValueError:
        print("Please enter a number, try  again.")
        return False


print()
print("How many days of a month in any year:")
print("—————————————————————————————————————————————")
month = input("Please enter a month (1-12): ")
check_user_input(month)
year = input("And now enter a year (i.e. 2011): ")
check_user_input(year)

month_num = str(month)
datetime_object = datetime.datetime.strptime(month_num, "%m")
full_month_name = datetime_object.strftime("%B")
num_days = monthrange(int(year), int(month))[1]

print("—————————————————————————————————————————————")
print(f"There are {num_days} days in {full_month_name} of the year {year}.")
print("—————————————————————————————————————————————")
