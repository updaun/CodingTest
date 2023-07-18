# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 문자열 섞기
# https://school.programmers.co.kr/learn/courses/30/lessons/181942


def solution(str1, str2):
    return "".join([i+j for i, j in zip(str1, str2)])


q = solution("aaaaa", "bbbbb")
assert q == "ababababab", "불일치"
print(q)
