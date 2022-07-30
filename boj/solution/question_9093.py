import sys
input = sys.stdin.readline
for i in range(int(input())):
    input_list = input().split()
    reverse_list = [i[::-1] for i in input_list]
    print(" ".join(map(str, reverse_list)))
