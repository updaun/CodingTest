import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

for _ in range(int(input())):
    s = list(map(int, list(input().rstrip())))
    for i in range(len(s)-1, 0, -1):
        if s[i] > s[i-1]:
            if i == len(s)-1:
                idx = len(s)-2
            else:
                idx = i-1
            a = s[:idx]
            b = s[idx:]
            b.sort()
            for j in range(len(b)):
                if b[j] > s[idx]:
                    a.append(b.pop(j))
                    a.extend(b)
                    print("".join(map(str, a)))
                    break
            break
    else:
        print("BIGGEST")

# 시간 초과
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**9)

# arr = []
# trigger = False
# def b(origin, s, idx):
#     global trigger
#     temp = s
#     s_list = sorted(list(temp))
#     if len(arr) == len(s):
#         if trigger and int("".join([s_list[i] for i in arr])) > int(s):
#             print(origin+"".join([s_list[i] for i in arr]))
#             trigger = False
#             return
#         if s == "".join([s_list[i] for i in arr]):
#             trigger = True
#         return
    
#     for i in range(len(s)):
#         if i not in arr:
#             arr.append(i)
#             b(origin, s, idx+1)
#             arr.pop()

# for _ in range(int(input())):
#     s = input().rstrip()
#     for i in range(len(s)-1, 0, -1):
#         if s[i] > s[i-1]:
#             b(s[:i-1], s[i-1:], 0)
#             break
#     else:
#         print("BIGGEST")