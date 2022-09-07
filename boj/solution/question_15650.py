# 시간 68ms
n, m = map(int, input().split())
arr = []

def backtracking():

    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return

    for i in range(1, n+1):
        if i not in arr:
            if len(arr) >= 1 and arr[-1] < i:
                arr.append(i)
                backtracking()
                arr.pop()
            elif len(arr) == 0:
                arr.append(i)
                backtracking()
                arr.pop()

backtracking()

"""
"""

# 시간 152ms
n, m = tuple(map(int, input().split()))

n_list = []
result = []

def n_search():
    if len(n_list) == m:
        if sorted(n_list) not in result:
            result.append(sorted(n_list))
            print(" ".join(map(str, n_list)))
        return
    for i in range(1, n+1):
        if i in n_list:
            continue
        n_list.append(i)
        n_search()
        n_list.pop()
n_search()