import sys
input = sys.stdin.readline
n, m = map(int, input().split())
eyfa = True
input_list = []
answer = []
for i in range(n):
    input_list.append(input().rstrip())
for i in range(n):
    answer.append(input().rstrip())
    temp = ''
    for j in range(m):
        temp += input_list[i][j]*2
    if temp != answer[i]:
        eyfa = False
        break
if eyfa:
    print("Eyfa")
else:
    print("Not Eyfa")