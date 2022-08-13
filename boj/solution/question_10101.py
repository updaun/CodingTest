import sys
input = sys.stdin.readline
triangle = []
for i in range(3):
    triangle.append(int(input()))
if sum(triangle) == 180:
    if len(set(triangle)) == 1:
        print("Equilateral")
    elif len(set(triangle)) == 2:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print('Error')