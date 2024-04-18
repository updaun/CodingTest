# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 문자열 잘라서 정렬하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181895


def solution(myString):
    return sorted([i for i in myString.split("x") if i != ""])


q = solution("axbxcxdx")
assert q == ["a","b","c","d"], "불일치"
print(q)

q = solution("dxccxbbbxaaaa")
assert q == ["aaaa","bbb","cc","d"], "불일치"
print(q)
