# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 배열 만들기 6
# https://school.programmers.co.kr/learn/courses/30/lessons/181859

def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        else:
            if stk[-1] == arr[i]:
                stk.pop()
                i += 1
            else:
                stk.append(arr[i])
                i += 1
    if len(stk) == 0:
        return [-1]
    return stk
        

q = solution([0, 1, 1, 1, 0])
assert q == [0, 1, 0], "불일치"
print(q)

q = solution([0, 1, 0, 1, 0])
assert q == [0, 1, 0, 1, 0], "불일치"
print(q)

q = solution([0, 1, 1, 0])
assert q == [-1], "불일치"
print(q)
