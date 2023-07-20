# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 날짜 비교하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181838#


def solution(date1, date2):
    d = [365, 30, 1]
    if sum([i*j for i,j in zip(date1, d)]) < sum([i*j for i,j in zip(date2, d)]):
        return 1
    return 0
    
# 다른 사람의 풀이
def solution(date1, date2):
    return int(date1 < date2)



q = solution([2021, 12, 28], [2021, 12, 29])
assert q == 1, "불일치"
print(q)

q = solution([1024, 10, 24], [1024, 10, 24])
assert q == 0, "불일치"
print(q)

q = solution([2010, 2, 10], [2009, 12, 10])
assert q == 0, "불일치"
print(q)