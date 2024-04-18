# 프로그래머스
# 코딩테스트 연습 > 2019 KAKAO BLIND RECRUITMENT > 실패율

def solution(N, stages):
    temp = 0
    p_list = []
    for i in range(1, N+1):
        stay = stages.count(i)
        if len(stages) - temp != 0:
            p = stay / (len(stages) - temp)
        else:
            p = 0
        temp += stay
        p_list.append(p)
    return [j[0] for j in sorted([[i, v] for i, v in enumerate(p_list, start=1)], key=lambda x:-x[1])]

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3])) # [3,4,2,1,5]
print(solution(4, [4,4,4,4,4])) # [4,1,2,3]