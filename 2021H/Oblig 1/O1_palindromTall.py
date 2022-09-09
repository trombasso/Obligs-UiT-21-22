number = int(input("Enter number:"))
temp = number
revers = 0

while number > 0:
    dig = number % 10
    revers = revers * 10 + dig
    number = number // 10
if temp == revers:
    print(str(temp) + " is a palindrome!")
else:
    print(str(temp) + " isn't a palindrome!")
