# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 문자열 뒤집기
# https://school.programmers.co.kr/learn/courses/30/lessons/181905


def solution(my_string, s, e):
    return my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]


q = solution("Progra21Sremm3", 6, 12)
assert q == "ProgrammerS123", "불일치"
print(q)

q = solution("Stanley1yelnatS", 4, 10)
assert q == "Stanley1yelnatS", "불일치"
print(q)
