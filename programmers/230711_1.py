# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 0 떼기
# https://school.programmers.co.kr/learn/courses/30/lessons/181847


def solution(n_str):
    for i in range(len(n_str)):
        if n_str[i] != "0":
            break
    return n_str[i:] 

# 다른 사람의 풀이
def solution(n_str):
    return n_str.lstrip('0')



q = solution("0010")
assert q == "10", "불일치"
print(q)

q = solution("854020")
assert q == "854020", "불일치"
print(q)
