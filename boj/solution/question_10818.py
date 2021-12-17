n = int(input())
number_list = list(map(int, input().split()))
max_num = number_list[0]
min_num = number_list[0]

for i in number_list:
    if max_num < i:max_num = i
    if min_num > i: min_num = i 

print(min_num, max_num)