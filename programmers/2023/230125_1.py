# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 귤 고르기

from collections import Counter
def solution(k, tangerine):
    answer = 0
    counter = Counter(tangerine)
    for i, v in enumerate(sorted(counter, key=lambda x:-counter[x]), start=1):
        answer += counter[v]
        if answer >= k:
            return i    
    return answer

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3])) # 3
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3])) # 2
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3])) # 1