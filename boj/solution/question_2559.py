import sys
N, K = list(map(int, sys.stdin.readline().split()))

# 시간 초과
n_list = list(map(int, sys.stdin.readline().split()))
target_list = []
for i in range(N-K):
    target_list.append(sum(n_list[i:i+K]))
print(max(target_list))
    