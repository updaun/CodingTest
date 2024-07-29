# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > A 강조하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181874?language=python3


def solution(myString):
    return myString.lower().replace("a", "A")

q = solution("abstract algebra")
assert q == "AbstrAct AlgebrA", "불일치"
print(q)

q = solution("PrOgRaMmErS")
assert q == "progrAmmers", "불일치"
print(q)
