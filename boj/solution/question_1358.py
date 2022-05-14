import sys
W,H,X,Y,P = list(map(int, sys.stdin.readline().split()))
count = 0
radius = H/2
left_circle_center = [X, Y+radius]
right_circle_center = [X+W, Y+radius]

for i in range(P):
    a, b = list(map(int, sys.stdin.readline().split()))
    if X <= a <= X+W and Y <= b <= Y+H:
        count +=1
        continue
    elif ((a-left_circle_center[0])**2 + (b-left_circle_center[1])**2) <= radius**2:
        count +=1
        continue
    elif ((a-right_circle_center[0])**2 + (b-right_circle_center[1])**2) <= radius**2:
        count +=1
        continue

print(count)