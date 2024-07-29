# 프로그래머스
# 코딩테스트 연습 > 완전탐색 > 피로도
# https://school.programmers.co.kr/learn/courses/30/lessons/87946

from itertools import permutations
def solution(k, dungeons):
    answer = -1
    for case in permutations(dungeons, len(dungeons)):
        result = 0
        hp = k
        for i in case:
            r, p = i
            if hp >= r:
                result += 1
                hp -= p
        answer = max(answer, result)
    return answer

print(80, [[80,20],[50,40],[30,10]]) # 3