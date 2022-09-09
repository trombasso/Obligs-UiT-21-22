from random import randint


def eq2text(lst):

    if lst[0] == 1:
        a = "x"
    elif lst[0] == -1:
        a = "-x"
    elif lst[0] == 0:
        a = ""
    else:
        a = f"{lst[0]}x"

    if lst[1] < 0:
        b = f" - {lst[1]-lst[1]*2}"
    else:
        b = f" + {lst[1]}"

    if lst[2] == 1:
        c = "x"
    elif lst[2] == -1:
        c = "-x"
    elif lst[2] == 0:
        c = ""
    else:
        c = f"{lst[2]}x"

    if lst[3] < 0:
        d = f" - {lst[3]-lst[3]*2}"
    else:
        d = f" + {lst[3]}"

    return f"{a}{b} = {c}{d}"


def make_eq():
    while True:
        try:
            lst = [randint(-9, 9) for x in range(4)]
            if ok(lst):
                break
            else:
                raise ValueError
        except ValueError:
            continue
    return lst


def ok(lst):
    a, b, c, d = lst[0], lst[1], lst[2], lst[3]
    if a == 0 or b == 0 or c == 0 or d == 0:
        return False
    elif a == c or b == d:
        return False
    else:
        return True


def make_n_eqs(n):
    lst = []
    for i in range(0, n):
        lst.append(make_eq())
    return lst


def make_test(students, n):
    dct = {}
    for i in students:
        dct[i] = make_n_eqs(n)
    return dct


def answer_questions(dct):
    while True:
        name = input("Enter your name: ")
        if name in dct:
            break

        print("again plaese.....")

    print("Please solve theese equations: ")

    for i in range(0, len(dct[name])):
        print(f"{chr(97 + i)}) {eq2text(dct[name][i])}")
        x = input("x = ")
        dct[name][i].append(x)


def main():
    tests = make_test(["Ola", "Kari", "Fredrik"], 5)
    answer_questions(tests)
    print(tests)


if __name__ == "__main__":
    main()
