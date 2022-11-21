import sys
input = sys.stdin.readline

def backtracking(cnt):

    if cnt == len(s):
        print(*answer, sep="")

    for k in visited:
        if visited[k]:
            visited[k] -= 1
            answer.append(k)
            backtracking(cnt + 1)
            visited[k] += 1
            answer.pop()

for i in range(int(input())):
    s = sorted(input().strip())
    visited = {}
    answer = []

    for i in s:
        if i in visited:
            visited[i] += 1
        else:
            visited[i] = 1
    
    backtracking(0)

# 시간초과
'''
import sys
input = sys.stdin.readline

def backtracking(arr, s, answer):

    if len(arr) == len(s):
        result = ""
        for i in arr:
            result += s[i]
        answer.append(result)
        return

    for i in range(len(s)):
        if i not in arr:
            arr.append(i)
            backtracking(arr, s, answer)
            arr.pop()

for i in range(int(input())):
    arr = []
    answer = []
    s = sorted(input().strip())
    backtracking(arr, s, answer)
    print(*sorted(list(set(answer))), sep="\n")
'''
