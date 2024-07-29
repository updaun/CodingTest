# 프로그래머스
# 코딩테스트 연습 > 완전탐색 > 최소직사각형


def solution(sizes):
    sizes = [sorted(size) for size in sizes]
    w = [i[0] for i in sizes]
    h = [i[1] for i in sizes]
    answer = max(w)*max(h)    
    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]])) # 4000
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])) # 120
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])) # 133