# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 햄버거 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/133502

def solution(ingredient):
    stack = []
    answer = 0
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1, 2, 3, 1]:
            answer += 1
            for i in range(4):
                stack.pop()
    return answer

# 시간초과 코드
def solution(ingredient):
    stack = []
    answer = 0
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1, 2, 3, 1]:
            answer += 1
            stack = stack[:-4] # 이 부분에서 시간을 많이 소비
    return answer


q = solution([2, 1, 1, 2, 3, 1, 2, 3, 1])
assert q == 2, "불일치"
print(q)

q = solution([1, 3, 2, 1, 2, 1, 3, 1, 2])
assert q == 0, "불일치"
print(q)

