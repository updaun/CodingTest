import sys
input = sys.stdin.readline
w_school = []
k_school = []
for i in range(10):
    w_school.append(int(input()))
for i in range(10):
    k_school.append(int(input()))
print(sum(sorted(w_school, reverse=True)[:3]), sum(sorted(k_school, reverse=True)[:3]))