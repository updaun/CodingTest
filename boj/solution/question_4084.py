import sys
input = sys.stdin.readline
while True:
    n_list = list(map(int, input().split()))
    if n_list == [0, 0, 0, 0]:
        break
    count = 0
    while True:
        if len(set(n_list)) == 1:
            print(count)
            break
        temp = []
        for i in range(3):
            temp.append(abs(n_list[i]-n_list[i+1]))
        temp.append(abs(n_list[-1]-n_list[0]))
        n_list = temp
        count += 1