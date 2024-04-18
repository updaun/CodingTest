# 프로그래머스
# 코딩테스트 연습 > 스택/큐 > 올바른 괄호

# 효율성 실패
def solution(s):  
    while "()" in s:
        s = s.replace("()", "")
    if s:
        return False
    return True

def solution(s):  
    count = 0
    l_count = 0
    r_count = 0
    for i in s:
        if i == "(":
            count += 1
            l_count += 1
        else:
            count -= 1
            r_count += 1
            if count < 0:
                return False
    if l_count != r_count:
        return False
    return True

print(solution("()()")) # True
print(solution("(())()")) # True
print(solution(")()(")) # False
print(solution("(()(")) # False