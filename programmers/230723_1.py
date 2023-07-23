# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 수열과 구간 쿼리 3
# https://school.programmers.co.kr/learn/courses/30/lessons/181924


def solution(arr, queries):
    for query in queries:
        s, f = query
        arr[f], arr[s] = arr[s], arr[f]
    return arr

# 다른 사람의 풀이
def solution(arr, queries):
    for s, f in queries:
        arr[f], arr[s] = arr[s], arr[f]
    return arr

q = solution([0, 1, 2, 3, 4], [[0, 3],[1, 2],[1, 4]])
assert q == [3, 4, 1, 0, 2], "불일치"
print(q)
