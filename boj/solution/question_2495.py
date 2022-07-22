import sys
for i in range(3):
    count_list = []
    target = sys.stdin.readline().rstrip()
    temp = 1
    for idx in range(len(target)-1):
        if target[idx] == target[idx+1]:
            temp += 1
        else:
            temp = 1
        count_list.append(temp)
    print(max(count_list))
