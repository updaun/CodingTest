# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 배열의 원소만큼 추가하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181861


def solution(arr):
    result = []
    for i in [[i]*i for i in arr]:
        result += i
    return result
    # return [i for i in arr for j in range(i)] # 한 줄 코드가 더 비효율적

q = solution([5, 1, 4])
assert q == [5, 5, 5, 5, 5, 1, 4, 4, 4, 4], "불일치"
print(q)

q = solution([6, 6])
assert q == [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6], "불일치"
print(q)

q = solution([1])
assert q == [1], "불일치"
print(q)

