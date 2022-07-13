import sys
X, Y = map(str, sys.stdin.readline().split())
result = int(X[::-1]) + int(Y[::-1])
target = str(result)[::-1]
for i in range(len(target)):
    if target[i] != "0":
        print(target[i:])
        break