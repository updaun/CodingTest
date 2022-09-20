# 신규 풀이 68ms
import sys
input = sys.stdin.readline
n = int(input())
n_list = sorted(list(map(int, input().split())))
print(sum([n_list[i]*(n-i) for i in range(n)]))

# 기존 풀이 72ms
# import sys
# n = int(sys.stdin.readline())
# result = 0
# raw = sorted(list(map(int, sys.stdin.readline().split())))
# for i in range(len(raw)):
#     result += sum(raw[:i+1])
# print(result)
