# 프로그래머스
# 코딩테스트 연습 > 2017 팁스타운 > 예상 대진표

def solution(n,a,b):
    answer = 0
    while True:
        answer += 1
        if a > 1:
            if a % 2 == 0:
                a //= 2
            else:
                a += 1
                a //= 2
        if b > 1:
            if b % 2 == 0:
                b //= 2
            else:
                b += 1
                b //= 2
        if a == b:
            break
    return answer

print(solution(8, 4, 7)) # 3