import sys
input = sys.stdin.readline
n, m = map(int, input().split())
b_list = []
for _ in range(n):
    p, i = map(int, input().split())
    p_list = sorted(list(map(int, input().split())), reverse=True)
    try:
        b_list.append(p_list[i-1])
    except:
        b_list.append(1)
b_list.sort()
for i in range(len(b_list)):
    m -= b_list[i]
    if m < 0:
        print(i)
        break
else:
    print(len(b_list))