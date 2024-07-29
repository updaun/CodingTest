# 프로그래머스
# 코딩테스트 연습 > Summer/Winter Coding(~2018) > 스킬트리
# https://school.programmers.co.kr/learn/courses/30/lessons/49993

from collections import deque


def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        q = deque(skill_tree)
        temp = deque(skill)
        while q:
            s = q.popleft()
            if s in temp and s == temp[0]:
                temp.popleft()
            elif s in temp and s != temp[0]:
                if not q:
                    answer -= 1
                break
        if not q:
            answer += 1
    return answer


q = solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])
assert q == 2, "불일치"
print(q)
