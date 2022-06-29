import sys
n = int(sys.stdin.readline())
correct_list = list(map(int, sys.stdin.readline().split()))
temp = 0
answer = correct_list[0]
for i in range(1, len(correct_list)):
    if correct_list[i] == 1 and correct_list[i-1] == 1:
        answer += correct_list[i]
        temp += 1
        answer += temp
    else:
        answer += correct_list[i]
        temp = 0
print(answer)

