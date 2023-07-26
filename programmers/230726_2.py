# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 문자열 겹쳐쓰기
# https://school.programmers.co.kr/learn/courses/30/lessons/181943


def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[len(my_string[:s] + overwrite_string):]

# 다른 사람의 풀이
def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]

q = solution("He11oWor1d", "lloWorl", 2)
assert q == "HelloWorld", "불일치"
print(q)

q = solution("Program29b8UYP", "merS123", 7)
assert q == "ProgrammerS123", "불일치"
print(q)
