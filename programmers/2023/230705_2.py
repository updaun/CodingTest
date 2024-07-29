# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > A 강조하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181874?language=python3


def solution(my_string, is_prefix):
    # return int(my_string[:len(is_prefix)] == is_prefix)
    # return 1 if my_string[:len(is_prefix)] == is_prefix else 0 
    # return int(my_string.startswith(is_prefix))
    return 1 if my_string.startswith(is_prefix) else 0 

q = solution("banana", "ban")
assert q == 1, "불일치"
print(q)

q = solution("banana", "nan")
assert q == 0, "불일치"
print(q)

q = solution("banana", "abcd")
assert q == 0, "불일치"
print(q)

q = solution("banana", "bananan")
assert q == 0, "불일치"
print(q)
