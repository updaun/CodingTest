# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 이차원 배열 대각선 순회하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181829


def solution(board, k):
    n, m = len(board), len(board[0])
    answer = 0
    for i in range(n):
        for j in range(m):
            if i+j <= k:
                answer += board[i][j]
    return answer


q = solution([[0, 1, 2],[1, 2, 3],[2, 3, 4],[3, 4, 5]], 2)
assert q == 8, "불일치"
print(q)
