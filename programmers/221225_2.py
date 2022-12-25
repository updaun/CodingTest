# 프로그래머스
# 코딩테스트 연습 > Summer/Winter Coding(~2018) > 예산


def solution(d, budget):
    d = sorted(d)
    answer = 0
    for i in range(len(d)):
        budget -= d[i]
        if budget == 0:
            return i+1
        elif budget < 0:
            return i
    return len(d)

print(solution([1,3,2,5,4], 9)) # 3
print(solution([2,2,3,3], 10)) # 4