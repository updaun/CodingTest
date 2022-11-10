import sys
input = sys.stdin.readline
n, m = map(int, input().split())
b_list = []
for _ in range(n):
    p, i = map(int, input().split())
    p_list = sorted(list(map(int, input().split())))
    try:
        b_list.append(p_list[i-1])
    except:
        b_list.append(1)
b_list.sort()
for i in range(len(b_list)):
    if m <= 0:
        result = i
        break
    m -= b_list[i]
print(result)
