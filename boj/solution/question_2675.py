n = int(input())
l = []
result = ''
for i in range(n):
    r, s = tuple(input().split(" "))
    l.append((int(r),s))
for num, str in l:
    for i in str:
        result += i*num
    result += '\n'
print(result)