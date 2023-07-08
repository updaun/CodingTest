# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 접미사인지 확인하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181908


def solution(my_string, is_suffix):
    return 1 if my_string[len(my_string)-len(is_suffix):] == is_suffix else 0
    # return int(my_string.endswith(is_suffix))

q = solution("banana", "ana")
assert q == 1, "불일치"
print(q)

q = solution("banana", "nan")
assert q == 0, "불일치"
print(q)

q = solution("banana", "wxyz")
assert q == 0, "불일치"
print(q)

q = solution("banana", "abanana")
assert q == 0, "불일치"
print(q)