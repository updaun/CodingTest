import sys
input = sys.stdin.readline

def binary_search(start, end, target):
    if end < start:
        return False
    mid = (start+end) // 2
    if n_list[mid] == target:
        return True
    elif target > n_list[mid]:
        return binary_search(mid+1, end, target)
    else:
        return binary_search(start, mid-1, target)

n = int(input())
n_list = list(map(int, input().split()))
t = int(input())
target_list = list(map(int, input().split()))
n_list = sorted(n_list)
for target in target_list:
    result = binary_search(0, n-1, target)
    if result:
        print(1)
    else:
        print(0)