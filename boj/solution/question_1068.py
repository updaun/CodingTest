# 78% 에서 실패되는 반례를 질문에서 발견, 놓치고 있는 부분 발견
# https://www.acmicpc.net/board/view/96949

import sys
input = sys.stdin.readline

n = int(input())
n_input = list(map(int, input().split()))
e = int(input())
v = [False for i in range(n)]

result = 0

def e_dfs(e):
    v[e] = True
    n_input[e] = -2
    for i in range(n):
        if v[i] == False and n_input[i] == e:
            e_dfs(i)

def dfs(curr):
    global result
    v[curr] = True

    if n_input.count(curr) == 0:
        result += 1
    
    for i in range(n):
        if v[i] == False and n_input[i] == curr:
            dfs(i)

e_dfs(e)
for i in range(n):
    if v[i] == False and n_input[i] == -1:
        dfs(i)

print(result)
