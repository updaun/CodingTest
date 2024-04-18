# 프로그래머스
# 코딩테스트 연습 > 정렬 > H-Index

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] >= i:
            answer = min(i+1, citations[i])
    return answer

print(solution([3, 0, 6, 1, 5])) # 3
print(solution([0, 0, 0, 0, 0])) # 0