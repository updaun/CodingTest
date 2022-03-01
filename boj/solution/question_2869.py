import math
A,B,V = tuple(map(int, input().split(" ")))
print(math.ceil((V-A)/(A-B))+1)