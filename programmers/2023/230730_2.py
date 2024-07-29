# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 문자 개수 세기
# https://school.programmers.co.kr/learn/courses/30/lessons/181902

def solution(my_string):
    answer = [0] * 52
    for s in my_string:
        if s.isupper():
            answer[ord(s)-65] += 1
        else:
            answer[ord(s)-97+26] += 1
    return answer


q = solution("Programmers")
assert q == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0], "불일치"
print(q)

