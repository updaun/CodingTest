# 프로그래머스
# 코딩테스트 연습 > 코딩테스트 입문 > 겹치는 선분의 길이

def solution(lines):
    answer = []
    for line in lines:
        start, end = line
        for i in range(start, end):
            answer.append(i)
    return sum([1 if answer.count(i) > 1 else 0 for i in set(answer)])


print(solution([[0, 1], [2, 5], [3, 9]])) # 2
print(solution([[-1, 1], [1, 3], [3, 9]])) # 0
print(solution([[0, 5], [3, 9], [1, 10]])) # 8
