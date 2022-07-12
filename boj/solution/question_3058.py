import sys
input = sys.stdin.readline
for i in range(int(input())):
    even_list = []
    for num in list(map(int, input().split())):
        if num % 2 == 0:
            even_list.append(num)
    print(sum(even_list), min(even_list))