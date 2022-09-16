import sys
input = sys.stdin.readline

d = []
d1 = []
d2 = []
d3 = []
d4 = []
s = []

for i in range(5):
    d1.append(list(map(int, input().split())))
for i in range(5):
    s += list(map(int, input().split()))
for i in range(5):
    d2.append([d1[j][i] for j in range(5)])
    d3.append(d1[i][i])
    d4.append(d1[4-i][i])
    
d = d1+d2+[d3]+[d4]

for i in range(25):
    for target in d:
        if s[i] in target:
            target.remove(s[i])
    if i > 10:
        count = 0
        for target in d:
            if len(target) == 0:
                count += 1
                if count > 2:
                    print(i+1)
                    sys.exit(0)
