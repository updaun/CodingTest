# 프로그래머스
# 코딩테스트 연습 > 깊이/너비 우선 탐색(DFS/BFS) > 네트워크
# https://school.programmers.co.kr/learn/courses/30/lessons/43162


from collections import deque


def bfs(matrix, start, visited):
    q = deque([start])
    visited[start] = True

    while q:
        node = q.popleft()
        for neighbor, is_connected in enumerate(matrix[node]):
            if is_connected and not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)


def solution(n, computers):
    visited = [False] * n
    answer = 0

    for i in range(n):
        if not visited[i]:
            bfs(computers, i, visited)
            answer += 1
    return answer


q = solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
assert q == 2, "불일치"
print(q)

q = solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])
assert q == 1, "불일치"
print(q)
