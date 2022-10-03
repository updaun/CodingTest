import sys
input = sys.stdin.readline
s = int(input())
e = 2 if s == 1 else 1
d = [[0]*3 for _ in range(3)]

def validate():
    for row in d:
        if row == [1, 1, 1]: return 1
        elif row == [2, 2, 2]: return 2
    cross = [] 
    r_cross = [] 
    for i in range(3):
        temp = []
        for j in range(3):
            temp.append(d[j][i])
            if i == j:
                cross.append(d[j][i])
            if abs(i-j) == 2 or (i==1 and j==1):
                r_cross.append(d[j][i])
        if temp == [1, 1, 1]: return 1
        elif temp == [2, 2, 2]: return 2
        if cross == [1, 1, 1]: return 1
        elif cross == [2, 2, 2]: return 2
        if r_cross == [1, 1, 1]: return 1
        elif r_cross == [2, 2, 2]: return 2
        
winner = 0
for i in range(9):
    x, y = map(int, input().split())
    if i % 2 == 0:
        d[x-1][y-1] = s
    else:
        d[x-1][y-1] = e
    if i > 2:
        winner = validate()
        if winner:
            print(winner)
            break

if not winner:
    print(0)
