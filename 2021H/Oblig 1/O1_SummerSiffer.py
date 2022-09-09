input_number = int(input("Legg inn et nummer mellom 0-1000: "))

# if input_number == 1000:
#     print("1")
# else:
#     c = input_number % 10
#     inputShortened = input_number // 10
#     b = inputShortened % 10
#     a = inputShortened // 10
#     print(a + b + c)

print((input_number // 10) // 10 + (input_number // 10) % 10 + input_number % 10)

# digits = []
# for digit in str(input_number):
#     digits.append(int(digit))
#     print(digits)

# print(sum(digits))

print(sum([int(x) for x in str(input_number)]))
