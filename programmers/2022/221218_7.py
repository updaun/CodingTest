# 프로그래머스
# 코딩테스트 연습 > 코딩테스트 입문 > 분수의 덧셈

def solution(denum1, num1, denum2, num2):
    a = denum1 * num2 + denum2 * num1
    b = num1*num2
    temp = 2
    while max(a, b) >= temp:
        if a % temp == 0 and b % temp == 0:
            a //= temp
            b //= temp
        else:
            temp += 1
    return [a, b]

print(solution(1, 2, 3, 4)) # [5, 4]
print(solution(9, 2, 1, 3)) # [29, 6]