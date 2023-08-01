# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 배열 만들기 4
# https://school.programmers.co.kr/learn/courses/30/lessons/181918

def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        else:
            if stk[-1] < arr[i]:
                stk.append(arr[i])
                i += 1
            else:
                stk.pop()
    return stk


q = solution([1, 4, 2, 5, 3])
assert q == [1, 2, 3], "불일치"
print(q)

