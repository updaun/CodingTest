# 프로그래머스
# 코딩테스트 연습 > 코딩테스트 입문 > 유한소수 판별하기

def to_divider(num):
    d_list = []
    temp = 2
    while num != 1:
        if num % temp == 0:
            num /= temp
            d_list.append(temp)
            temp = 2
        else:
            temp += 1
    return d_list

def solution(a, b):
    if b % a == 0:
        b = b // a
        a = 1
    a_list = to_divider(a)
    b_list = to_divider(b)
    for i in a_list:
        if i in b_list:
            b_list.remove(i)
        
    b_set = set(b_list)
    if len(b_set) == 0 or b_set == set([2]) or b_set == set([5]) or b_set == set([2, 5]):
        return 1
    
    return 2


print(solution(7, 20)) # 1
print(solution(11, 22)) # 1
print(solution(12, 21)) # 2
print(solution(12, 36)) # 2
print(solution(3500, 500)) # 1