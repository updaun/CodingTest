# 프로그래머스
# 코딩테스트 연습 > Summer/Winter Coding(~2018) > 점프와 순간 이동

# 십진수를 1씩 올려가며 2진수를 찾는 방식은 시간이 오래걸리게 된다.
# def solution(n):
#     ans = 0
    
#     while n:
#         temp = 0
#         while 2**temp <= n:
#             temp += 1
#         n -= 2**(temp-1)
#         ans += 1
    
#     return ans

def solution(n):
    ans = 0
    
    while n > 0:
        if n >= 2:
            temp = len(bin(n)[2:])
        else:
            temp = 1
        n -= 2**(temp-1)
        ans += 1
    
    return ans


print(solution(5)) # 2
print(solution(6)) # 2
print(solution(5000)) # 5