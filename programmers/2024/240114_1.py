# 프로그래머스
# 프로그래밍 강의 > PCCE 기출문제 > [PCCE 기출문제] 9번 / 이웃한 칸
# https://school.programmers.co.kr/learn/courses/30/lessons/250125

def solution(board, h, w):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    bx, by = len(board), len(board[0])
    cur = board[h][w]
    for i in range(4):
        nx = h + dx[i]
        ny = w + dy[i]
        if nx < 0 or nx >= bx or ny < 0 or ny >= by:
            continue
        if cur == board[nx][ny]:
            answer += 1
    return answer

q = solution([["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]], 1, 1)
assert q == 2, "불일치"
print(q)

q = solution([["yellow", "green", "blue"], ["blue", "green", "yellow"], ["yellow", "blue", "blue"]], 0, 1)
assert q == 1, "불일치"
print(q)

