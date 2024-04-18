# 프로그래머스
# 코딩테스트 연습 > 2018 KAKAO BLIND RECRUITMENT > [1차] 캐시

from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    if cacheSize == 0:
        return len(cities)*5
    for i in cities:
        if i.lower() in cache:
            answer += 1
            cache.remove(i.lower())
            cache.append(i.lower())
        else:
            answer += 5
            if len(cache) < cacheSize:
                cache.append(i.lower())
            else:
                cache.popleft()
                cache.append(i.lower())
    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])) # 50
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])) # 21
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])) # 60
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])) # 52
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"])) # 16
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])) # 25