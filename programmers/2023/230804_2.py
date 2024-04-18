# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 문자열 여러 번 뒤집기
# https://school.programmers.co.kr/learn/courses/30/lessons/181913

def solution(my_string, queries):
    answer = my_string
    for s, e in queries:
        answer = answer[:s] + answer[s:e+1][::-1] + answer[e+1:]
    return answer

q = solution("rermgorpsam", [[2, 3], [0, 7], [5, 9], [6, 10]])
assert q == "programmers", "불일치"
print(q)
