# 프로그래머스
# 코딩테스트 연습 > 코딩테스트 입문 > 최대공약수와 최소공배수

def solution(n, m):
    a, b = min(n, m), max(n, m)
    g = []
    answer = []
    for i in range(1, a+1):
        if a % i == 0 and b % i == 0:
            g.append(i)
    answer.append(g[-1])
    for j in range(g[-1], a*b+1):
        if j % a == 0 and j % b == 0:
            answer.append(j)
            break
    return answer

print(solution(3, 12)) # [3, 12]
print(solution(2, 5)) # [1, 10]