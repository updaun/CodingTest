# 프로그래머스
# 코딩테스트 연습 > 코딩테스트 입문 > 팩토리얼
def solution(n):
    answer = 0
    factorials = [1]
    for i in range(2, 11):
        factorials.append(factorials[-1] * i)
    while answer != 10 and factorials[answer] <= n:
        answer += 1    
    return answer

# 3628800	10
# 7	3