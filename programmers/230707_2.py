# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 꼬리 문자열
# https://school.programmers.co.kr/learn/courses/30/lessons/181841


def solution(str_list, ex):
    return "".join([i for i in str_list if ex not in i])

q = solution(["abc", "def", "ghi"], "ef")
assert q == "abcghi", "불일치"
print(q)

q = solution(["abc", "bbc", "cbc"], "c")
assert q == "", "불일치"
print(q)
