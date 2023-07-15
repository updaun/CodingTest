# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 가까운 1 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/181898


def solution(arr, idx):
    for i, v in enumerate(arr[idx:]):
        if v == 1:
            return idx + i
    return -1


q = solution([0, 0, 0, 1], 1)
assert q == 3, "불일치"
print(q)

q = solution([1, 0, 0, 1, 0, 0], 4)
assert q == -1, "불일치"
print(q)

q = solution([1, 1, 1, 1, 0], 3)
assert q == 3, "불일치"
print(q)
