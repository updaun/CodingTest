# 프로그래머스
# 코딩테스트 연습 > 깊이/너비 우선 탐색(DFS/BFS) > 단어 변환
# https://school.programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque

def is_one_diff(word1, word2):
    diff_count = 0 
    for char1, char2 in zip(word1, word2):
        if char1 != char2:
            diff_count += 1
            if diff_count > 1:
                return False
    return diff_count == 1

def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = set()
    queue = deque([(begin, 0)])

    while queue:
        current_word, step = queue.popleft()
        if current_word == target:
            return step
        
        for word in words:
            if word not in visited and is_one_diff(current_word, word):
                visited.add(word)
                queue.append((word, step+1))
    return 0


q = solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
assert q == 4, "불일치"
print(q)

q = solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
assert q == 0, "불일치"
print(q)
