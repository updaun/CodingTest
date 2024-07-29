# 프로그래머스
# 코딩테스트 연습 > 그래프 > 가장 먼 노드
# https://school.programmers.co.kr/learn/courses/30/lessons/49189?language=python3

from collections import defaultdict, deque

def solution(n, edge):
    graph = defaultdict(list)
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)

    queue = deque([1])
    distances = {i: -1 for i in range(1, n+1)}
    distances[1] = 0
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if distances[neighbor] == -1:
                queue.append(neighbor)
                distances[neighbor] = distances[node] + 1
    
    max_distance = max(distances.values())
    farthest_nodes = [node for node, distance in distances.items() if distance == max_distance]
    
    return len(farthest_nodes)

q = solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
assert q == 3, f"잘못된 결과: {q}"
print(q)
