# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 기사단원의 무기

def get_divisor(number, limit, power):
    divisorsList = []
    for i in range(1, int(number**(1/2)) + 1):
        if (number % i == 0):
            divisorsList.append(i) 
            if (i**2 != number) : 
                divisorsList.append(number // i)
            if len(divisorsList) > limit:
                return power
    return len(divisorsList)
    

def solution(number, limit, power):
    answer = []
    for i in range(1, number+1):
        v = get_divisor(i, limit, power)
        answer.append(v)
    return sum(answer)