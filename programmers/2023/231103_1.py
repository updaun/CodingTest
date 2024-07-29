# 프로그래머스
# 프로그래밍 강의 > PCCE 모의고사 > [PCCE 모의고사] 9번
# https://school.programmers.co.kr/learn/courses/19275/lessons/240614

def solution(times, n):
    answer = []
    for s in range(len(times)-n+1):
        answer.append(sum(times[s:s+n]))
    return max(answer)

q = solution([4, 6, 3, 1, 0, 5, 9, 0, 1, 3], 4)
assert q == 15, "불일치"
print(q)
