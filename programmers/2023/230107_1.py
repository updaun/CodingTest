# 프로그래머스
# 코딩테스트 연습 > 해시 > 위장

# 조합으로 처음에 풀이 시도 -> 시간초과
from itertools import combinations
def solution(clothes):
    answer = 0
    d = {}
    for cloth in clothes:
        name, kind = cloth
        if kind in d.keys():
            d[kind] += 1
        else:
            d[kind] = 1
            
    for i in range(1, len(d.keys())+1):
        
        for case in combinations(d.values(), i):
            temp = 1
            for i in case:
                temp *= i
            answer += temp
    
    return answer

# 수학적 수식을 적용한 방법
# https://school.programmers.co.kr/questions/33347
def solution(clothes):
    answer = 1
    d = {}
    for cloth in clothes:
        name, kind = cloth
        if kind in d.keys():
            d[kind] += 1
        else:
            d[kind] = 1            
    for i in d.values():
        answer *= (i+1)
    return answer-1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])) # 5
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])) # 3