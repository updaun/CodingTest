# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 배열 조각하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181893

def solution(arr, query):
    for i, n in enumerate(query):
        if i % 2 == 0:
            arr = arr[:n+1]
        else:
            arr = arr[n:]
    return arr


q = solution([0, 1, 2, 3, 4, 5], [4, 1, 2])
assert q == [1, 2, 3], "불일치"
print(q)
