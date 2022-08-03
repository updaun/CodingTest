c = 1000-int(input())
k = [500, 100, 50, 10, 5, 1]
result = 0
for i in k:
    count, c = divmod(c, i)
    result += count
print(result)