month = int(input("Enter month (1-12): "))
year = int(input("Enter year (i.e. 2020): "))
is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

monthname = [
    "",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
if is_leap_year:
    days_in_month[2] = 29

if is_leap_year:
    print(f"The year {year} is a leap year!")
print(f"There are {days_in_month[month]} days in {monthname[month]} of {year}.")
