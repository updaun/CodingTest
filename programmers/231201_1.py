# 프로그래머스
# 코딩테스트 연습 > Summer/Winter Coding(~2018) > 방문 길이
# https://school.programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    visited = set()
    d = {"U":(0,1), "D":(0,-1), "R":(1,0), "L":(-1,0)}
    x, y = 0, 0
    for dir in dirs:
        nx, ny = x + d[dir][0], y + d[dir][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.add((x,y,nx,ny))
            visited.add((nx,ny,x,y))
            x, y = nx, ny
    return len(visited)//2

q = solution("ULURRDLLU")
assert q == 7, "불일치"
print(q)

q = solution("LULLLLLLU")
assert q == 7, "불일치"
print(q)
