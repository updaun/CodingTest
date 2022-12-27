# 프로그래머스
# 코딩테스트 연습 > 2017 팁스타운 > 짝지어 제거하기

# 재귀함수로 문제 풀이 : recursion error 발생
def check(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            s.pop(i)
            s.pop(i)
            check(s)
            break
    return s

def solution(s):
    answer = check(list(s))
    if answer:
        return 0    
    return 1

# stack을 활용한 문제 풀이
def solution(s):
    stack = []
    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
        else:
            if stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
    if stack:
        return 0    
    return 1