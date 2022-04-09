import sys
n = int(sys.stdin.readline())
coordinate_list = list(map(int, sys.stdin.readline().split()))
sorted_list = sorted(list(set(coordinate_list)))
coordinate_dict = {sorted_list[i] : i for i in range(len(sorted_list))}
for i in coordinate_list:
    sys.stdout.write(str(coordinate_dict[i]) + " ")