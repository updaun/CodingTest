import sys
N, M = list(map(int, sys.stdin.readline().split()))
S = []
c_list = []
count = 0
for i in range(N):
    S.append(sys.stdin.readline().strip())
for i in range(M):
    c_list.append(sys.stdin.readline().strip())
# print(len(set(S).intersection(set(c_list))))
for word in c_list:
    if word in S:
        count+=1
print(count) 