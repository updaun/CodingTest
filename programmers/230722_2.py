# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 글자 지우기
# https://school.programmers.co.kr/learn/courses/30/lessons/181900


def solution(my_string, indices):
    answer = ''
    for i, s in enumerate(my_string):
        if i not in indices:
            answer += s
    return answer


q = solution("apporoograpemmemprs", [1, 16, 6, 15, 0, 10, 11, 3])
assert q == "programmers", "불일치"
print(q)
