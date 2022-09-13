# 이전 풀이
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())

# n_list = sorted(list(map(int, input().split())))

# arr = []

# def backtracking():

#     if len(arr) == m:
#         print(*arr)
#         return

#     for i in range(n):
#         if len(arr) > 0 :
#             if n_list[i] not in arr and arr[-1] < n_list[i]:
#                 arr.append(n_list[i])
#                 backtracking()
#                 arr.pop()
#         else:
#             arr.append(n_list[i])
#             backtracking()
#             arr.pop()

# backtracking()

# 질문 이후 풀이

n, m = map(int, input().split())
arr = []

def backtracking(a):

    if len(arr) == m:
        print(*arr)
        return

    for i in range(a+1, n+1):
        arr.append(i)
        backtracking(i)
        arr.pop()


backtracking(0)