# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 배열 만들기 2
# https://school.programmers.co.kr/learn/courses/30/lessons/181921

def solution(l, r):
    temp = [bin(i)[2:].replace("1", "5") for i in range(2**6)]
    answer = []
    for i in temp:
        n = int(i)
        if l <= n <= r:
            answer.append(n)
        if n > r:
            break
    if len(answer) == 0:
        return [-1]
    return answer

q = solution(5, 555)
assert q == [5, 50, 55, 500, 505, 550, 555], "불일치"
print(q)

q = solution(10, 20)
assert q == [-1], "불일치"
print(q)
