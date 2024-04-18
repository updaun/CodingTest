# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 수열과 구간 쿼리 2
# https://school.programmers.co.kr/learn/courses/30/lessons/181923

def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        temp = []
        for i in range(s,e+1):
            t = arr[i]
            if t > k:
                temp.append(t)
        if len(temp) == 0:
            answer.append(-1)
        else:
            answer.append(min(temp))
    return answer

q = solution([0, 1, 2, 4, 3], [[0, 4, 2],[0, 3, 2],[0, 2, 2]])
assert q == [3, 4, -1], "불일치"
print(q)
