# DP(72ms)
n = int(input())
d = [5001]*(n+5)
d[3] = d[5] = 1
for i in range(6, n+1):
    d[i] = min(d[i-3], d[i-5]) + 1
print(d[n] if d[n] < 5001 else -1)

# 그리디 알고리즘(68ms)
sugar = int(input())
bag = 0
while sugar >= 0:
    if sugar % 5 == 0:
        bag += (sugar // 5)
        print(bag)
        break
    sugar -= 3
    bag += 1
else:
    print(-1)