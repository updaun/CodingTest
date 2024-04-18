# 프로그래머스
# 코딩테스트 연습 > 깊이/너비 우선 탐색(DFS/BFS) > 게임 맵 최단거리
# https://school.programmers.co.kr/learn/courses/30/lessons/1844


from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(n, m, i, j, visited, maps):
    
    q = deque([(i, j)])
    distance = {(i, j): 1}
    while q:
        x, y = q.popleft()
        
        visited[x][y] = 1
        
        for ix, iy in zip(dx, dy):
            nx, ny = x+ix, y+iy
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny]:
                if (nx, ny) == (n-1, m-1):
                    return distance[(x, y)] + 1
                q.append((nx, ny))
                distance[(nx, ny)] = distance[(x, y)] + 1
                visited[nx][ny] = True
    return -1
                    
                    
def solution(maps):
    answer = -1
    n, m = len(maps), len(maps[0])
    visited = [[0]*m for i in range(n)]
    answer = bfs(n, m, 0, 0, visited, maps)
                      
    return answer

q = solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])
assert q == 11, "불일치"
print(q)

q = solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])
assert q == -1, "불일치"
print(q)
