n = int(input())
for i in range(n):
    t = input().lower()
    if t == t[::-1]: 
        print('Yes')
    else:
        print('No')