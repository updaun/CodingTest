# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 접미사 배열
# https://school.programmers.co.kr/learn/courses/30/lessons/181909


def solution(my_string):
    return sorted([my_string[i:] for i in range(len(my_string))])

q = solution("banana")
assert q == ["a", "ana", "anana", "banana", "na", "nana"], "불일치"
print(q)

q = solution("programmers")
assert q == ["ammers", "ers", "grammers", "mers", "mmers", "ogrammers", "programmers", "rammers", "rogrammers", "rs", "s"], "불일치"
print(q)
