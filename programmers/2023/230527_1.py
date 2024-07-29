# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 배열에서 문자열 대소문자 변환하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181875


def solution(strArr):
    return [i.lower() if idx%2==0 else i.upper() for idx, i in enumerate(strArr)]

q = solution(["AAA","BBB","CCC","DDD"])
assert q == ["aaa","BBB","ccc","DDD"], "불일치"
print(q)

q = solution(["aBc","AbC"])
assert q == ["abc","ABC"], "불일치"
print(q)
