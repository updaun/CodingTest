import sys
T = int(sys.stdin.readline())
for i in range(T):
    math_list = list(sys.stdin.readline().split())

    result = float(math_list[0])
    for i in range(1, len(math_list)):
        c = math_list[i]
        if c == '@':
            result *= 3
        elif c == '%':
            result += 5
        elif c == '#':
            result -= 7
    print("{:.2f}".format(result))
