# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 무작위로 K개의 수 뽑기
# https://school.programmers.co.kr/learn/courses/30/lessons/181858

from collections import Counter

def solution(arr, k):
    answer = list(Counter(arr).keys())[:k]
    if len(answer) < k:
        answer += [-1] * (k-len(answer))
    return answer

# Counter 없이 dict.fromkeys로 중복 제거
def solution(arr, k):
    answer = list(dict.fromkeys(arr))[:k]
    if len(answer) < k:
        answer += [-1] * (k-len(answer))
    return answer

q = solution([0, 1, 1, 2, 2, 3], 3)
assert q == [0, 1, 2], "불일치"
print(q)

q = solution([0, 1, 1, 1, 1], 4)
assert q == [0, 1, -1, -1], "불일치"
print(q)
