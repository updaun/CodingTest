import sys
odd_list = []
for i in range(7):
    num = int(sys.stdin.readline())
    if num % 2 != 0:
        odd_list.append(num)
if len(odd_list) != 0:
    print(sum(odd_list))
    print(min(odd_list))
else:
    print(-1)