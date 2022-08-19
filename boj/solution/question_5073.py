import sys
input = sys.stdin.readline
while True:
    t = list(map(int, input().split()))
    if t == [0, 0, 0]:
        break
    t = sorted(t)
    if t[0]+t[1] <= t[2]:
        print("Invalid")
    else:
        if len(set(t)) == 1:
            print("Equilateral")
        elif len(set(t)) == 2:
            print("Isosceles")
        else:
            print("Scalene")
            