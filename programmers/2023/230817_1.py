# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 롤케이크 자르기
# https://school.programmers.co.kr/learn/courses/30/lessons/132265


from collections import Counter
def solution(topping):
    answer = 0
    d = Counter(topping)
    b = set()
    for i in topping:
        d[i] -= 1
        if d[i] == 0:
            del d[i]
        b.add(i)
        if len(b) == len(d):
            answer += 1
    return answer


q = solution([1, 2, 1, 3, 1, 4, 1, 2])
assert q == 2, "불일치"
print(q)

q = solution([1, 2, 3, 1, 4])
assert q == 0, "불일치"
print(q)
