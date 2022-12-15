# 프로그래머스
# 코딩테스트 연습 > 코딩테스트 입문 > 소인수분해
def solution(n):
    answer = []
    temp = 2
    while n != 1:
        while n % temp != 0:
            temp += 1
        n, _ = divmod(n, temp)
        answer.append(temp)
    answer = sorted(list(set(answer)))
    return answer

print(solution(17))
print(solution(420))