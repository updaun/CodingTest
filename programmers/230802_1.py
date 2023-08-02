# 프로그래머스
# 코딩테스트 연습 > 스택/큐 > 올바른 괄호
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):  
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True


q = solution("()()")
assert q == True, "불일치"
print(q)

q = solution("(())()")
assert q == True, "불일치"
print(q)

q = solution(")()(")
assert q == False, "불일치"
print(q)

q = solution("(()(")
assert q == False, "불일치"
print(q)

