import sys
n = int(sys.stdin.readline())
for i in range(n):
    candy, child = list(map(int, sys.stdin.readline().split()))
    print(f"You get {candy//child} piece(s) and your dad gets {candy%child} piece(s).")