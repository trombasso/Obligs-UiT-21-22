def methodX(n):
    if n > 0:
        print(n % 10)
        methodX(n // 10)


def factorial(n):
    return n * factorial(n - 1)  # Recursive call


# methodX(100)


# factorial(3)


# def main():
#     n = int(input("Enter a non-negative integer: "))
#     print("Factorial of", n, "is", factorial(n))


#     # Return the factorial for a specified number
# def factorial(n):
#     if n == 0: # Base case
#         return 1
#     else:
#         return n * factorial(n - 1) # Recursive call


# main() # Call the main function


def fib(index):
    if index == 0:  # Base case
        return 0
    elif index == 1:  # Base case
        return 1
    else:  # Reduction and recursive calls
        return fib(index - 2)


for i in range(0, 20):
    print(fib(i))
