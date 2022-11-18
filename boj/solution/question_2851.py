import sys
input = sys.stdin.readline
temp = 0
n_list = []
for i in range(10):
    temp += int(input())
    if temp-100 == 0:
        n_list.append([abs(temp-100), 1])
    else:
        n_list.append([abs(temp-100), (temp-100)//abs(temp-100)])
n_list.sort(key=lambda x:(x[0], -x[1]))
print(abs(n_list[0][0]+n_list[0][1]*100))
