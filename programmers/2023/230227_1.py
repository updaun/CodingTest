# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 할인 행사
# https://school.programmers.co.kr/learn/courses/30/lessons/131127

def solution(want, number, discount):
    answer = 0
    wants = []
    for i, j in zip(want, number):
        wants += [i]*j
    t = sorted(wants)
    for i in range(len(discount)-9):
        if sorted(discount[i:i+10]) == t:
            answer += 1
    return answer


q = solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple",
             "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])
assert q == 3, "불일치"
print(q)

q = solution(["apple"], [10], ["banana", "banana", "banana", "banana",
             "banana", "banana", "banana", "banana", "banana", "banana"])
assert q == 0, "불일치"
print(q)
