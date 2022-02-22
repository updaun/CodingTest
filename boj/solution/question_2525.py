h, m = tuple(map(int, input().split(" ")))
c = int(input())
hour = h+c//60
min = m+c%60
while min>=60:
    min -= 60
    hour += 1
while hour >= 24:
    hour -= 24
print(hour, min)