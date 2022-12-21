# 프로그래머스
# 코딩테스트 연습 > 코딩테스트 입문 > 약수의 개수와 덧셈

def check(num):
    arr = []
    temp = 1
    while temp <= num:
        if num % temp == 0:
            arr.append(temp)
        temp += 1
    if len(set(arr)) % 2 == 0:
        return True
    return False

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if check(i):
            answer += i
        else:
            answer -= i
    return answer

print(solution(13, 17)) # 43
print(solution(24, 27)) # 52