# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 조건에 맞게 수열 변환하기 2
# https://school.programmers.co.kr/learn/courses/30/lessons/181881

def solution(arr):
    answer = 0
    temp = []
    while True:
        temp = []
        for i in arr:
            if i >= 50 and i % 2 == 0:
                temp.append(i//2)
            elif i < 50 and i % 2 != 0:
                temp.append(i*2+1)
            else:
                temp.append(i)
        if arr == temp:
            break
        answer += 1
        arr = temp
    return answer


q = solution([1, 2, 3, 100, 99, 98])
assert q == 5, "불일치"
print(q)

