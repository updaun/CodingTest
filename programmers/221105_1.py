# 2022 Winter Coding - 겨울방학 스타트업 인턴 프로그램
def solution(line):
    trigger = False
    temp = ''
    answer = ''
    for s in line:
        if s == temp:
            trigger = True
        else:
            trigger = False
        temp = s
        if trigger and answer[-1] != "*":
            answer += "*"
        elif not trigger:
            answer += s
    return answer