import sys
day = int(sys.stdin.readline())
car_list = list(map(int, sys.stdin.readline().split()))
count = 0
for car in car_list:
    if str(car)[-1] == str(day):
        count += 1
print(count)