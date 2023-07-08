# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 문자열 바꿔서 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/181864


def solution(myString, pat):
    return 1 if pat in "".join(["B" if i=="A" else "A" for i in myString]) else 0

q = solution("ABBAA", "AABB")
assert q == 1, "불일치"
print(q)

q = solution("ABAB", "ABAB")
assert q == 0, "불일치"
print(q)
