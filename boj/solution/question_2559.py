import sys
N, K = list(map(int, sys.stdin.readline().split()))
temp_list = list(map(int, sys.stdin.readline().split()))
k_day_list = [sum(temp_list[:K])]
for i in range(1, N-K+1):
    sum_k = k_day_list[-1] + temp_list[i+K-1] - temp_list[i-1]
    k_day_list.append(sum_k)
print(max(k_day_list))
