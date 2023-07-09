# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 배열의 길이에 따라 다른 연산하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181854


def solution(arr, n):
    if len(arr) % 2 == 0:
        return [v if i % 2 == 0 else v+n for i, v in enumerate(arr)]
    return [v if i % 2 != 0 else v+n for i, v in enumerate(arr)]

q = solution([49, 12, 100, 276, 33], 27)
assert q == [76, 12, 127, 276, 60], "불일치"
print(q)

q = solution([444, 555, 666, 777], 100)
assert q == [444, 655, 666, 877], "불일치"
print(q)
