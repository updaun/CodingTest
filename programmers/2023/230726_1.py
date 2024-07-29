# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 문자열이 몇 번 등장하는지 세기
# https://school.programmers.co.kr/learn/courses/30/lessons/181871


def solution(myString, pat):
    answer = 0
    for i in range(0, len(myString)-len(pat)+1):
        if myString[i:i+len(pat)] == pat:
            answer += 1
    return answer

# 다른 사람의 풀이
def solution(myString, pat):
    return sum(myString[i:i + len(pat)] == pat for i in range(len(myString)))

q = solution("banana", "ana")
assert q == 2, "불일치"
print(q)

q = solution("aaaa", "aa")
assert q == 3, "불일치"
print(q)
