# 프로그래머스
# 코딩테스트 연습 > 스택/큐 > 주식가격
# https://school.programmers.co.kr/learn/courses/30/lessons/42584

# 시간 초과 코드
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)-1):
        temp = prices[i]
        for j in prices[i+1:]:
            if j >= temp:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer

# 스택을 활용한 풀이


def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i, price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i-j
        stack.append(i)
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j
    return answer


q = solution([1, 2, 3, 2, 3])
assert q == [4, 3, 1, 1, 0], "불일치"
print(q)
