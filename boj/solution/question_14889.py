# 4604ms
import sys

n = int(sys.stdin.readline())
table = []
team1 = [0]*int(n/2)
team2 = [0]*int(n/2)
pick = [0]*n
answer = sys.maxsize

def update():
    global answer
    team1_size = 0
    team2_size = 0
    for i in range(n):
        if pick[i] == 0:
            team1[team1_size] = i
            team1_size += 1
        else:
            team2[team2_size] = i
            team2_size += 1
    sum_1 = 0
    sum_2 = 0
    for i in range(int(n/2)):
        for j in range(i+1, int(n/2)):
            sum_1 += table[team1[i]][team1[j]] + table[team1[j]][team1[i]]
            sum_2 += table[team2[i]][team2[j]] + table[team2[j]][team2[i]]
    if answer > abs(sum_1 - sum_2):
        answer = abs(sum_1 - sum_2)

def dfs(cur, pick_count):
    if pick_count == n/2:
        update()
        return None
    
    for i in range(cur, n):
        pick[i] = 1
        dfs(i + 1, pick_count + 1)
        pick[i] = 0

for i in range(n):
    table.append(list(map(int, sys.stdin.readline().split())))

dfs(0, 0)
print(answer)

# 5812ms
import sys
input = sys.stdin.readline

n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]

start = []
link = []
answer = sys.maxsize

def backtracking(index):
    global answer
    start_num = 0
    link_num = 0
    if index == n//2:
        for i in range(n):
            if i not in start:
                link.append(i)
        
        for i in range(n//2-1):
            for j in range(i+1, n//2):
                start_num += d[start[i]][start[j]] + d[start[j]][start[i]]
                link_num += d[link[i]][link[j]] + d[link[j]][link[i]]
        answer = min(answer, abs(start_num-link_num))
        link.clear()
        return

    for i in range(n):
        if i in start:
            continue
        if len(start)>0 and start[-1]>i:
            continue
        start.append(i)
        backtracking(index+1)
        start.pop()

backtracking(0)
print(answer)