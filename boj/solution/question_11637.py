import sys
input = sys.stdin.readline
for i in range(int(input())):
    c_list = []
    for j in range(int(input())):
        c_list.append(int(input()))
    if c_list.count(max(c_list)) > 1:
        print("no winner")
    elif max(c_list)/sum(c_list) > 0.5:
        print(f"majority winner {c_list.index(max(c_list))+1}")
    elif max(c_list)/sum(c_list) <= 0.5:
        print(f"minority winner {c_list.index(max(c_list))+1}")

