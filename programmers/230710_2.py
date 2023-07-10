# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > l로 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/181834


def solution(myString):
    return "".join([i if ord(i) > 108 else "l" for i in myString])    


q = solution("abcdevwxyz")
assert q == "lllllvwxyz", "불일치"
print(q)

q = solution("jjnnllkkmm")
assert q == "llnnllllmm", "불일치"
print(q)
