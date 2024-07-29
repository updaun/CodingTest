# 프로그래머스
# 프로그래밍 강의 > PCCE 기출문제 > [PCCE 기출문제] 9번
# https://school.programmers.co.kr/learn/courses/19274/lessons/240604

def solution(board, h, w):
    answer = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    n = len(board)
    target = board[h][w]
    for i in range(4):
        nx = h + dx[i]
        ny = w + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if target == board[nx][ny]:
                answer += 1
    return answer

q = solution([["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]], 1, 1)
assert q == 2, "불일치"
print(q)

q = solution([["yellow", "green", "blue"], ["blue", "green", "yellow"], ["yellow", "blue", "blue"]], 0, 1)
assert q == 1, "불일치"
print(q)
