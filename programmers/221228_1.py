# 프로그래머스
# 코딩테스트 연습 > 완전탐색 > 카펫

def solution(brown, yellow):
    temp = 1
    while yellow >= temp:
        if yellow % temp == 0:
            w, h = yellow // temp, temp
            if 2*(w+2)+2*h == brown:
                return [w+2, h+2]
        temp += 1
        
print(solution(10, 2)) # [4, 3]
print(solution(8, 1)) # [3, 3]
print(solution(24, 24)) # [8, 6]