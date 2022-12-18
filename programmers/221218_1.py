# 프로그래머스
# 코딩테스트 연습 > 코딩테스트 입문 > 저주의 숫자 3

def solution(n):
    answer = 0
    i = 0
    while True:
        i += 1
        if i % 3 == 0 or "3" in str(i):
            continue
        answer += 1
        if answer == n:
            return i

print(solution(15)) # 25
print(solution(40)) # 76