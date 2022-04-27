import sys
R = int(sys.stdin.readline())

for i in range(R):
    r = int(sys.stdin.readline())
    clothes = dict()
    result = 1
    for j in range(r):
        _, category = list(sys.stdin.readline().split())
        if category not in clothes:
            clothes[category] = 1
        else:
            clothes[category] += 1
    for i in list(clothes.values()):
        result *= (i+1)
    print(result-1)