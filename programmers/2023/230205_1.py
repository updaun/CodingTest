# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 과일 장수

def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(len(score)//m):
        box = score[m*i:m*i+m]
        answer += min(box)*m
    return answer
    # return sum(sorted(score)[len(score)%m::m])*m

print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1])) # 8
print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2])) # 33