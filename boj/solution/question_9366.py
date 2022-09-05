import sys
input = sys.stdin.readline
for i in range(int(input())):
    a, b, c = sorted(list(map(int, input().split())))
    if a+b <= c:
        print(f"Case #{i+1}: invalid!")
    else:
        if a == b and b == c:
            print(f"Case #{i+1}: equilateral")
        elif a == b or b == c:
            print(f"Case #{i+1}: isosceles")
        else:
            print(f"Case #{i+1}: scalene")
            