# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 피보나치 수


def solution(d, budget):
    d = sorted(d)
    for i in range(len(d)):
        budget -= d[i]
        if budget == 0:
            return i+1
        elif budget < 0:
            return i
    return len(d)

print(solution(3)) # 2
print(solution(5)) # 5