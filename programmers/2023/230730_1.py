# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 2의 영역
# https://school.programmers.co.kr/learn/courses/30/lessons/181894


def solution(arr):
    if 2 not in arr:
        return [-1]    
    return arr[arr.index(2): len(arr)-arr[::-1].index(2)]


q = solution([1, 2, 1, 4, 5, 2, 9])
assert q == [2, 1, 4, 5, 2], "불일치"
print(q)

q = solution([1, 2, 1])
assert q == [2], "불일치"
print(q)

q = solution([1, 1, 1])
assert q == [-1], "불일치"
print(q)

q = solution([1, 2, 1, 2, 1, 10, 2, 1])
assert q == [2, 1, 2, 1, 10, 2], "불일치"
print(q)
