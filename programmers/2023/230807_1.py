# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 그림 확대
# https://school.programmers.co.kr/learn/courses/30/lessons/181836

def solution(picture, k):
    answer = []
    for p in picture:
        temp = "".join([i*k for i in p])
        for i in range(k):
            answer.append(temp)
    return answer

q = solution([".xx...xx.", "x..x.x..x", "x...x...x", ".x.....x.", "..x...x..", "...x.x...", "....x...."], 2)
assert q == 	["..xxxx......xxxx..", "..xxxx......xxxx..", "xx....xx..xx....xx", "xx....xx..xx....xx", "xx......xx......xx", "xx......xx......xx", "..xx..........xx..", "..xx..........xx..", "....xx......xx....", "....xx......xx....", "......xx..xx......", "......xx..xx......", "........xx........", "........xx........"], "불일치"
print(q)

q = solution(["x.x", ".x.", "x.x"], 3)
assert q == ["xxx...xxx", "xxx...xxx", "xxx...xxx", "...xxx...", "...xxx...", "...xxx...", "xxx...xxx", "xxx...xxx", "xxx...xxx"], "불일치"
print(q)
