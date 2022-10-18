# https://claude-u.tistory.com/m/376
# 고민하다 답봄
import sys
input = sys.stdin.readline

t = [(n*(n+1))//2 for n in range(1, 45)]
d = [0] * 1001

for i in t:
    for j in t:
        for k in t:
            if i+j+k < 1001:
                d[i+j+k] = 1

for i in range(int(input())):
    print(d[int(input())])