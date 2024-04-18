# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 세로 읽기
# https://school.programmers.co.kr/learn/courses/30/lessons/181904


def solution(my_string, m, c):
    return "".join([my_string[i] for i in range(c-1, len(my_string), m)])

# 다른 사람의 풀이
def solution(s, m, c):
    return s[c-1::m]


q = solution("ihrhbakrfpndopljhygc", 4, 2)
assert q == "happy", "불일치"
print(q)

q = solution("programmers", 1, 1)
assert q == "programmers", "불일치"
print(q)
