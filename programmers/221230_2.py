# 프로그래머스
# 코딩테스트 연습 > 연습문제 > N개의 최소공배수

def solution(arr):
    q = sorted(arr, reverse=True)
    answer = q.pop()
    while q:
        temp = q.pop()
        a = min(answer, temp)
        b = max(answer, temp)
        x, y = a, b
        while y:
            x, y = y, x%y
            answer = (a*b)//x
    return answer


print(solution([2,6,8,14])) # 168
print(solution([1,2,3])) # 6