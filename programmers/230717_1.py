# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 배열 만들기 3
# https://school.programmers.co.kr/learn/courses/30/lessons/181895


def solution(arr, intervals):
    answer = []
    for i in intervals:
        answer += arr[i[0]:i[1]+1]
    return answer


q = solution([1, 2, 3, 4, 5], [[1, 3], [0, 4]])
assert q == [2, 3, 4, 1, 2, 3, 4, 5], "불일치"
print(q)
