import sys
num_list = []
for i in range(5):
    num_list.append(int(sys.stdin.readline()))
print(int(sum(num_list)/len(num_list)))
print(sorted(num_list)[int(len(num_list)/2)])