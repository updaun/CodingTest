# 프로그래머스
# 프로그래밍 강의 > PCCP 모의고사 1회 > [PCCP 모의고사 1] 1번
# https://school.programmers.co.kr/learn/courses/15008/lessons/121683

def solution(input_string):
    answer = ''
    stack = []
    for s in input_string:
        if stack and s == stack[-1]:
            continue
        stack.append(s)
    temp = set()
    for i in stack:
        if i not in temp:
            temp.add(i)
        else:
            answer += i
    if answer:
        return "".join(sorted(list(set(answer))))
    return "N"

q = solution("edeaaabbccd")
assert q == "de", "불일치"
print(q)

q = solution("eeddee")
assert q == "e", "불일치"
print(q)

q = solution("string")
assert q == "N", "불일치"
print(q)

q = solution("zbzbz")
assert q == "bz", "불일치"
print(q)
