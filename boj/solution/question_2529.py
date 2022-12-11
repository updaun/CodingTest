# https://great-park.tistory.com/38
import sys
input = sys.stdin.readline
n = int(input())
c_list = list(input().split())
visited = [False] * 10
answer = []

def check(i, j, k):
    if k == "<":
        return i < j
    else:
        return i > j   

def backtracking(result, depth):

    if depth == n+1:
        answer.append(result)
        return

    for i in range(10):
        if not visited[i]:
            if depth==0 or check(result[-1], str(i), c_list[depth-1]):
                visited[i] = True
                backtracking(result+str(i), depth+1)
                visited[i] = False

backtracking("", 0)
print(answer[-1])
print(answer[0])

# 시간초과
# n = int(input())
# c_list = list(input().split())
# arr = []
# result = []

# def check(num_list, c_list):
#     for i in range(n):
#         if c_list[i] == "<":
#             if num_list[i] > num_list[i+1]:
#                 return False
#         else:
#             if num_list[i] < num_list[i+1]:
#                 return False
#     return True

# def backtracking(num, arr):

#     if len(arr) == n+1:
#         if check(arr, c_list):
#             result.append("".join(map(str, arr)))
#             return

#     for i in range(10):
#         if i not in arr:
#             arr.append(i)
#             backtracking(num, arr)
#             arr.pop()

# backtracking(n, arr)
# print(result[-1])
# print(result[0])