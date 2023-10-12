# 프로그래머스
# 코딩테스트 연습 > 완전탐색 > 모음사전
# https://school.programmers.co.kr/learn/courses/30/lessons/84512

from itertools import product

def solution(word):
    words = []
    for i in range(1, 6):
        for c in product(["A", "E", "I", "O", "U"], repeat=i):            
            words.append("".join(list(c)))
    words.sort()
    return words.index(word) + 1
                    
def solution(word):
    answer = 0
    for i, n in enumerate(word):
        answer += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n) + 1
    return answer

q = solution("AAAAE")
assert q == 6, "불일치"
print(q)

q = solution("AAAE")
assert q == 10, "불일치"
print(q)

q = solution("I")
assert q == 1563, "불일치"
print(q)

q = solution("EIO")
assert q == 1189, "불일치"
print(q)

