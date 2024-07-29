# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 부분 문자열 이어 붙여 문자열 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/181911


def solution(my_strings, parts):
    return "".join([i[j[0]:j[1]+1] for i, j in zip(my_strings, parts)])


q = solution(["progressive", "hamburger", "hammer", "ahocorasick"], [[0, 4], [1, 2], [3, 5], [7, 7]])
assert q == "programmers", "불일치"
print(q)
