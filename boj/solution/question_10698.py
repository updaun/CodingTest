import sys
input = sys.stdin.readline
for i in range(int(input())):
    trigger = False
    c = input().split() 
    if c[1] == '+':
        trigger = int(c[0]) + int(c[2]) == int(c[-1])
    else:
        trigger = int(c[0]) - int(c[2]) == int(c[-1])
    if trigger:
        print(f"Case {i+1}: YES")
    else:
        print(f"Case {i+1}: NO")