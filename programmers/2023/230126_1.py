# 프로그래머스
# 코딩테스트 연습 > 깊이/너비 우선 탐색(DFS/BFS) > 타겟 넘버

def solution(numbers, target):
    answer = 0
    def dfs(numbers, target, index, s):
        if index == len(numbers):
            if s == target:
                nonlocal answer
                answer += 1
            return

        dfs(numbers, target, index+1, s+numbers[index])
        dfs(numbers, target, index+1, s-numbers[index])
    dfs(numbers, target,0,0)
    return answer

print(solution([1, 1, 1, 1, 1], 3)) # 5
print(solution([4, 1, 2, 1], 4)) # 2