# 프로그래머스
# 코딩테스트 연습 > 코딩테스트 입문 > 평행

def solution(dots):
    for i in range(1, len(dots)):
        c_dots = dots.copy()
        line = []
        line.append(c_dots.pop(i))
        line.append(c_dots.pop(0))
        p1, p2 = c_dots
        p3, p4 = line
        a1 = (p2[1]-p1[1])/(p2[0]-p1[0])
        a2 = (p4[1]-p3[1])/(p4[0]-p3[0])
        if a1 == a2:
            return 1
    return 0

print(solution([[1, 4], [9, 2], [3, 8], [11, 6]])) # 1
print(solution([[3, 5], [4, 1], [2, 4], [5, 10]])) # 0