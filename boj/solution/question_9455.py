# 속도 개선을 위해 다른 사람 풀이 참고 (172ms)
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    m, n = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(m)]
    temp = []
    for i in range(n):
        temp.append([d[j][i] for j in range(m)])
    result = 0 
    for j in range(n):
        count = 0
        for i in range(m-1, -1, -1):
            if d[i][j] == 1:
                result += count
            else:
                count += 1
    print(result)

# 내 풀이 (1544ms)
# import sys
# input = sys.stdin.readline

# def cal(s):
#     count = 0
#     while s != sorted(s):
#         for i in range(len(s)-1):
#             if s[i] == 1 and s[i+1] == 0:
#                 s.insert(i+1, s.pop(i))
#                 count += 1
#     return count

# for _ in range(int(input())):
#     m, n = map(int, input().split())
#     d = [list(map(int, input().split())) for _ in range(m)]
#     temp = []
#     for i in range(n):
#         temp.append([d[j][i] for j in range(m)])
#     result = 0 
#     for case in temp:
#         result += cal(case)
#     print(result)
