# 프로그래머스
# 코딩테스트 연습 > 코딩테스트 입문 > 다음에 올 숫자

def solution(common):
    answer = 0
    p_num = []
    m_num = []
    for i in range(len(common)-1):
        p_num.append(common[i+1] - common[i])
        if common[i] != 0:
            m_num.append(common[i+1] // common[i])
    if len(set(p_num)) == 1:
        return common[-1] + p_num[0]
    elif len(set(m_num)) == 1:
        return int(common[-1] * m_num[0])
    
print(solution([1, 2, 3, 4])) # 5
print(solution([2, 4, 8])) # 16