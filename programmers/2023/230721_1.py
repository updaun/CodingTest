# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 수열과 구간 쿼리 1
# https://school.programmers.co.kr/learn/courses/30/lessons/181883


def solution(arr, queries):
    for query in queries:
        temp = [1 if i in range(query[0], query[1]+1) else 0 for i in range(len(arr))]
        arr = [i+j for i,j in zip(arr, temp)]
    return arr
    
# 다른 사람의 풀이
def solution(arr, queries):
    for (s, e) in queries:
        arr = [a+1 if s <= i <= e else a for i, a in enumerate(arr)]
    return arr


q = solution([0, 1, 2, 3, 4], [[0, 1],[1, 2],[2, 3]])
assert q == [1, 3, 4, 4, 4], "불일치"
print(q)
