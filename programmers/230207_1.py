# 프로그래머스
# 코딩테스트 연습 > 힙(Heap) > 더 맵게

# 시간초과
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    for i in range(len(scoville)):
        if sum([1 if i>=K else 0 for i in scoville])//len(scoville) == 1:
            break
        try:
            food_a = heapq.heappop(scoville)
            food_b = heapq.heappop(scoville)
        except:
            return -1
        heapq.heappush(scoville, food_b*2+food_a)    
        answer += 1
    return answer

# 개선 코드
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0]<K:        
        food_a = heapq.heappop(scoville)
        food_b = heapq.heappop(scoville)
        heapq.heappush(scoville, food_b*2+food_a)    
        answer += 1
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7)) # 2