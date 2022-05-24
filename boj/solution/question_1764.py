import sys
N,M = list(map(int, sys.stdin.readline().split()))
n_list = []
m_list = []
for i in range(N):
    n_list.append(sys.stdin.readline().strip())
for i in range(M):
    m_list.append(sys.stdin.readline().strip())
target = sorted(list(set(n_list).intersection(set(m_list))))
print(len(target))
print("\n".join(map(str, target)))
