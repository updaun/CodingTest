# 프로그래머스
# 코딩테스트 연습 > 월간 코드 챌린지 시즌3 > n^2 배열 자르기

# 시간초과1
def solution(n, left, right):
    answer = []
    for i in range(1, n+1):
        if len(answer) > right+1:
            break
        answer += [i if k < i else k for k in range(1, n+1)]
    return answer[left: right+1]

# 시간초과2
def solution(n, left, right):
    answer = []
    for i in range(1, n+1):
        if len(answer) > right+1:
            break
        answer += [i]*i
        answer += list(range(i+1, n+1))
        # answer += [i if k < i else k for k in range(1, n+1)]
    # print(answer)
    return answer[left: right+1]

# 시간초과3
def solution(n, left, right):
    answer = []
    for i in range(1, n+1):
        if len(answer) > right+1:
            break
        answer += [a+b for a,b in zip(list(range(1, n+1)), list(range(1, i))[::-1]+[0]*n)]
    return answer[left: right+1]

# 풀이 참고 https://school.programmers.co.kr/questions/26196
def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        row, col = divmod(i, n)
        if row > col :
            answer.append(row+1)
        else:
            answer.append(col+1)
    return answer

print(solution(3, 2, 5)) # [3,2,2,3]
print(solution(4, 7, 14)) # [4,3,3,3,4,4,4,4]