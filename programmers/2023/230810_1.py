# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 코드 처리하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181932

def solution(code):
    answer = ''
    mode = 0
    for i, v in enumerate(code):
        if mode == 0:
            if v == "1":
                mode = 1
            else:
                if i % 2 == 0:
                    answer += v
        else:
            if v == "1":
                mode = 0
            else:
                if i % 2 != 0:
                    answer += v
    if answer == "":
        return "EMPTY"
    return answer

# 다른 사람의 풀이
def solution(code):
    return "".join(code.split("1"))[::2] or "EMPTY"

q = solution("abc1abc1abc")
assert q == "acbac", "불일치"
print(q)
