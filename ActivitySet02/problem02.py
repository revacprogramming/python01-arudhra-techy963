

def input2no():
    a, b = map(int, input("Input? ").split())
    return a, b


def add(a, b):
    c = a + b
    return c


def output(a, b, sum2):
    print(a, "+", b, " is ",sum2)


def main():
    a, b = input2no( )
    sum2 = add(a, b)
    output(a, b, sum2)


main()
