import sys
input = sys.stdin.readline
for i in range(int(input())):
    n = int(input())
    n_dict = {}
    temp = 2
    while True:
        if n == 1:
            break
        if n % temp == 0:
            n /= temp
            if temp in n_dict.keys():
                n_dict[temp] += 1
            else:
                n_dict[temp] = 1
        else:
            temp += 1
    result = sorted(n_dict)
    for i in result:
        print(i, n_dict[i])
    