num_list = list(input().split(" "))
num_list = [int(i[::-1]) for i in num_list]
print(max(num_list))