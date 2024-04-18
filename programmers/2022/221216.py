# 프로그래머스
# 코딩테스트 연습 > 코딩테스트 입문 > 문자열 밀기

def solution(A, B):
    a_list = list(A)
    b_list = list(B)
    if A==B:
        return 0
    for i in range(len(A)):
        a_list.insert(0, a_list.pop())
        if a_list == b_list:
            return i+1
    return -1

print(solution("hello","ohell"))
print(solution("apple","elppa"))
