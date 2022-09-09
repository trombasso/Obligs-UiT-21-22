# def methodX(n):
#     if n == 1:
#         return n
#     else:
#         return n + methodX(n - 1)


# print(methodX(4))


# def main():
#     lst = [1, 2, 3, 4, 5]
#     methodX(lst, 5)


# def methodX(lst, n):
#     print(lst[n - 1], end=" ")
#     methodX(lst, n - 1)


# main()


# def isPalindrome(s):
#     return isPalindromeHelper(s, 0, len(s) - 1)


# def isPalindromeHelper(s, low, high):
#     if high <= low:  # Base case
#         return True
#     elif s[low] != s[high]:  # Base case
#         return False
#     else:
#         return isPalindromeHelper(s, low + 1, high - 1)


# print(isPalindrome("agnes i senga"))


# def isPalindrome(s):
#     if len(s) <= 1:  # Base case
#         return True
#     elif s[0] != s[len(s) - 1]:  # Base case
#         return False
#     else:
#         return isPalindrome(s[1 : len(s) - 1])


# print(isPalindrome("agnes i senga"))


# -------A
def mainA():
    methodX(5)


def methodX(n):
    if n > 1:
        print(n - 1, end=" ")
        methodX(n - 1)


# -------B
def mainB():
    methodXX(5)


def methodXX(n):
    while n > 1:
        print(n - 1, end=" ")
        methodXX(n - 1)


# mainA()
# print("-----")
# mainB()


def main():
    print(methodX(2, 0))


def methodX(n, result):
    if n == 0:
        return 0
    else:
        return methodX(n - 1, n + result)


main()
