import sys
S = sys.stdin.readline().strip()
s_list = []
for i in range(1, len(S)+1):
    for j in range(len(S)):
        if j+i <= len(S):
            s_list.append(S[j:j+i])
print(len(set(s_list)))
