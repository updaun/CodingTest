import sys
n, k = list(map(int, sys.stdin.readline().split()))
coin_list = []
for i in range(n):
    coin_list.append(int(sys.stdin.readline()))

count = 0
for i in coin_list[::-1]:
    if k >= i:
        count += k//i
        k = k%i
    if k == 0:
        break
print(count)