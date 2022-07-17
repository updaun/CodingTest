import sys
input = sys.stdin.readline
while True:
    target = input().rstrip()
    if target == "END":
        break
    print(target[::-1])