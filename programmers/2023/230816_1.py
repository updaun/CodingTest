# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 롤케이크 자르기
# https://school.programmers.co.kr/learn/courses/30/lessons/132265


def solution(topping):
    answer = 0
    total = len(set(topping))
    for i in range(total//2, len(topping)):
        l, r = len(set(topping[:i])), len(set(topping[i:]))
        if l == r:
            answer += 1
    return answer


q = solution([1, 2, 1, 3, 1, 4, 1, 2])
assert q == 2, "불일치"
print(q)

q = solution([1, 2, 3, 1, 4])
assert q == 0, "불일치"
print(q)
