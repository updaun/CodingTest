# boj
# 수학은 비대면강의입니다
# https://www.acmicpc.net/problem/19532

a, b, c, d, e, f = map(int, input().split())
D = a*e - b*d
Dx = c*e - b*f
Dy = a*f - c*d
print(int(Dx/D), int(Dy/D))


# 1 3 -1 4 1 7

# 2 -1

# 2 5 8 3 -4 -11

# -1 2