# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 문정사각형으로 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/181830

def solution(arr):
    l = len(arr)
    r = len(arr[0])
    if l > r:
        diff = l-r
        for t in arr:
            for i in range(diff):
                t.append(0)
    elif l < r:
        diff = r-l
        for i in range(diff):
            arr.append([0]*r)
    return arr

q = solution([[572, 22, 37], [287, 726, 384], [85, 137, 292], [487, 13, 876]])
assert q == [[572, 22, 37, 0], [287, 726, 384, 0], [85, 137, 292, 0], [487, 13, 876, 0]], "불일치"
print(q)

q = solution([[57, 192, 534, 2], [9, 345, 192, 999]])
assert q == [[57, 192, 534, 2], [9, 345, 192, 999], [0, 0, 0, 0], [0, 0, 0, 0]], "불일치"
print(q)

q = solution([[1, 2], [3, 4]]	)
assert q == [[1, 2], [3, 4]], "불일치"
print(q)
