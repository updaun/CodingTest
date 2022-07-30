import sys
input = sys.stdin.readline
for i in range(int(input())):
    target = int(input())
    temp = 1
    c_list = []
    while temp <= int(target/2):
        if temp != target-temp:
            c_list.append(f"{temp} {target-temp}")
        temp += 1
    print(f"Pairs for {target}: "+", ".join(map(str, c_list)))