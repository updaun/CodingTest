# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 둘만의 암호
# https://school.programmers.co.kr/learn/courses/30/lessons/155652

def solution(s, skip, index):
    answer = ''
    a = [chr(i) for i in range(97, 123) if not chr(i) in skip]     
    for i in s:
        answer += a[(a.index(i) + index)%len(a)]
    return answer


q = solution("aukks", "wbqd", 5)
assert q == "happy", "불일치"
print(q)

