# https://programmers.co.kr/learn/courses/30/lessons/77484

# 코딩테스트 연습
# 2021 Dev-Matching: 웹 백엔드 개발자(상반기)
# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    zero_count = lottos.count(0)
    inter = len(set(lottos).intersection(set(win_nums)))
    best_match = inter + zero_count
    if best_match == 0:
        best_match = 1
    worst_match = inter
    if worst_match == 0:
        worst_match = 1
    answer = [7-best_match, 7-worst_match]
    return answer