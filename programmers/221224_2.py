# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 숫자의 표현

def solution(n):
    count = 0
    for i in range(1, n+1):
        temp = i
        total = 0
        while total <= n:
            if total == n:
                count += 1
                break
            total += temp
            temp += 1
    return count
        
print(solution(15)) # 5