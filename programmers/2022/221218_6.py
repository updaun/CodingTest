# 프로그래머스
# 코딩테스트 연습 > 코딩테스트 입문 > 연속된 수의 합

def solution(num, total):
    mid = total//num
    answer = [mid]
    temp = 1
    while len(answer) < num:
        if len(answer) % 2 == 0:
            answer.append(mid - temp)
            temp += 1
        else:
            answer.append(mid + temp)
    return sorted(answer)

print(solution(3, 12)) # [3, 4, 5]
print(solution(5, 15)) # [1, 2, 3, 4, 5]
print(solution(4, 14)) # [2, 3, 4, 5]
print(solution(5, 5)) # [-1, 0, 1, 2, 3]
