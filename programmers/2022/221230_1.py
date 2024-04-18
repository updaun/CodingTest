# 프로그래머스
# 코딩테스트 연습 > 월간 코드 챌린지 시즌1 > 두 개 뽑아서 더하기

from itertools import combinations

def solution(numbers):
    answer = []
    for i in combinations(numbers, 2):
        if sum(i) not in answer:
            answer.append(sum(i))
    return sorted(answer)


print(solution([2,1,3,4,1])) # 	[2,3,4,5,6,7]
print(solution([5,0,2,7])) # [2,5,7,9,12]