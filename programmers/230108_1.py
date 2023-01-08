# 프로그래머스
# 코딩테스트 연습 > 월간 코드 챌린지 시즌2 > 괄호 회전하기

from collections import deque

# 스택 방식의 구현 접근 -> 반례 발생
def check(s_list):
    s_c, m_c, l_c = 0, 0, 0
    for s in s_list:
        if s == "[":
            l_c += 1
        elif s == "]":
            l_c -= 1
            if l_c < 0:
                return 0
            if l_c == 0 and (m_c != 0 or s_c != 0):
                return 0
        elif s == "{":
            m_c += 1
        elif s == "}":
            m_c -= 1
            if m_c < 0:
                return 0
            if m_c == 0 and (s_c != 0 or l_c != 0):
                return 0
        elif s == "(":
            s_c += 1
        elif s == ")":
            s_c -= 1
            if s_c < 0:
                return 0
            if s_c == 0 and (m_c != 0 or l_c != 0):
                return 0
    if s_c == 0 and m_c == 0 and l_c == 0:
        return 1
    return 0

# replace로 제거 반복
def check(s):
    while "()" in s or "{}" in s or "[]" in s:
        if "()" in s:
            s = s.replace("()", "")
        if "{}" in s:
            s = s.replace("{}", "")
        if "[]" in s:
            s = s.replace("[]", "")
    if s:
        return 0
    return 1
        
def solution(s):
    answer = 0
    d= deque([i for i in s])
    for i in range(len(d)):
        answer += check("".join(d))
        d.rotate()
        
    return answer

print(solution("[](){}")) # 3
print(solution("}]()[{")) # 3
print(solution("[)(]")) # 0
print(solution("[(])")) # 0
print(solution("}}}")) # 0