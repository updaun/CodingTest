# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 수 조작하기 1
# https://school.programmers.co.kr/learn/courses/30/lessons/181926


def solution(n, control):
    values = [1, -1, 10, -10]
    counts = [control.count(i) for i in ["w", "s", "d", "a"]]
    return n + sum([a*b for a, b in zip(values, counts)])

q = solution(0, "wsdawsdassw")
assert q == -1, "불일치"
print(q)

# 테스트 1 〉	통과 (0.15ms, 10.1MB)
# 테스트 2 〉	통과 (1.07ms, 10.4MB)
# 테스트 3 〉	통과 (0.11ms, 10.1MB)
# 테스트 4 〉	통과 (0.57ms, 10.4MB)
# 테스트 5 〉	통과 (1.09ms, 10.2MB)
# 테스트 6 〉	통과 (0.85ms, 10.3MB)
# 테스트 7 〉	통과 (0.44ms, 10.2MB)
# 테스트 8 〉	통과 (0.23ms, 10.2MB)
# 테스트 9 〉	통과 (0.88ms, 10.3MB)
# 테스트 10 〉  통과 (0.13ms, 10.2MB)
# 테스트 11 〉  통과 (0.22ms, 10.3MB)

# 단순 풀이 시 시간이 오래 걸리므로 효율적인 방법을 항상 고민하기
def solution(n, control):
    for i in control:
        if i == "w":
            n += 1
        elif i == "s":
            n -= 1
        elif i == "d":
            n += 10
        else:
            n -= 10
    return n

# 테스트 1 〉	통과 (1.25ms, 10MB)
# 테스트 2 〉	통과 (8.95ms, 10.2MB)
# 테스트 3 〉	통과 (0.75ms, 10.1MB)
# 테스트 4 〉	통과 (5.17ms, 10.2MB)
# 테스트 5 〉	통과 (8.77ms, 10.4MB)
# 테스트 6 〉	통과 (7.16ms, 10.2MB)
# 테스트 7 〉	통과 (3.88ms, 10.4MB)
# 테스트 8 〉	통과 (1.52ms, 10.3MB)
# 테스트 9 〉	통과 (7.28ms, 10.2MB)
# 테스트 10 〉  통과 (1.92ms, 10.2MB)
# 테스트 11 〉  통과 (3.94ms, 10.2MB)