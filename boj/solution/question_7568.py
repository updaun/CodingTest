n = int(input())
d_list = []
for i in range(n):
    w, h = tuple(map(int, input().split()))
    d_list.append([w, h])

for i in range(len(d_list)):
    rank = 1
    for j in range(len(d_list)):
        if d_list[j][0] > d_list[i][0] and d_list[j][1] > d_list[i][1]:
            rank += 1
    print(rank, end=' ')