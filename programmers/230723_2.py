# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/181872


def solution(myString, pat):
    return myString[:myString.rfind(pat)+len(pat)]

# 다른 사람의 풀이
def solution(myString, pat):
    return myString[:len(myString) - myString[::-1].index(pat[::-1])]

q = solution("AbCdEFG", "dE")
assert q == "AbCdE", "불일치"
print(q)

q = solution("AAAAaaaa", "a")
assert q == "AAAAaaaa", "불일치"
print(q)
