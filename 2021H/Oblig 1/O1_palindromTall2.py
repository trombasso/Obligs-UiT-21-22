number = input("Enter a number: ")
number_reversed = number[::-1]
if number == number_reversed:
    print(f"The number {number} is a palindrome!")
else:
    print(f"{number} is not a palindrome.")
