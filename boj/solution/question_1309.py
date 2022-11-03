# https://hooongs.tistory.com/151
n = int(input())
d = [1, 3] + [0]*n
for i in range(2, n+1):
    if i > 1:
        d[i] = (2*d[i-1] + d[i-2])%9901
print(d[n])