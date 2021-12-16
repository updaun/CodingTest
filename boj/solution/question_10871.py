n, m = map(int, input().split())
number_list = list(map(int, input().split()))
for i in number_list:
    if i < m:
        print(i, end=" ")