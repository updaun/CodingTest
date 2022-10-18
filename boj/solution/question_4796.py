import sys
input = sys.stdin.readline
i = 1
while True:
    l, p, v = map(int, input().split())
    if (l, p, v) == (0, 0, 0):
        break
    temp, v = divmod(v, p)
    result = temp*l
    if v > l:
        result += l
    else:
        result += v
    print(f"Case {i}: {result}")
    i += 1
