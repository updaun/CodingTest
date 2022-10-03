n = int(input())
d = [i**2 for i in range(501)]
count = 0
for a in range(1, len(d)):
    for b in range(1, len(d)):
        if a > b:
            if d[a]-d[b] == n:
                count += 1
print(count)