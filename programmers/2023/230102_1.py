# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 멀리 뛰기

def solution(n):
    d = [1, 1]
    for i in range(2, n+1):
        temp = d[i-1] + d[i-2]
        d.append(temp)    
    return d[n] % 1234567

print(solution(4)) # 5
print(solution(3)) # 3