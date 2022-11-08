import sys
input = sys.stdin.readline
n,p = map(int, input().split())
cycle = []
start = n
while True:
    result = start * n % p
    if result in cycle:
        print(len(cycle) - cycle.index(result))
        break
    cycle.append(result)
    start = result

# 57%에서 실패
# import sys
# input = sys.stdin.readline

# n,p = map(int, input().split())
# cycle = []
# start = n
# while True:
#     result = start * n % p
#     if len(cycle)//3 == len(set(cycle)) and len(cycle) != 0:
#         break
#     cycle.append(result)
#     start = result    
# print(len(set(cycle)))