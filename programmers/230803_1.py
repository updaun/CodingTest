# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 왼쪽 오른쪽
# https://school.programmers.co.kr/learn/courses/30/lessons/181890

def solution(str_list):
    if "l" not in str_list and "r" not in str_list:
        return []
    else:
        a = str_list.index("l") if "l" in str_list else None
        b = str_list.index("r") if "r" in str_list else None
        if a is None:
            return str_list[b+1:]
        if b is None:
            return str_list[:a]
        if a < b:
            return str_list[:a]
        else:
            return str_list[b+1:]
        
# 다른 사람의 풀이
def solution(str_list):
    for i in range(len(str_list)):
        if str_list[i]=='l': return str_list[:i]
        elif str_list[i]=='r': return str_list[i+1:]
    return []


q = solution(["u", "u", "l", "r"])
assert q == ["u", "u"], "불일치"
print(q)

q = solution(["l"])
assert q == [], "불일치"
print(q)
