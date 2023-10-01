# 구름LEVEL
# GameJam
# https://level.goorm.io/exam/195692/gamejam/quiz/1

n = int(input())
rg, cg = map(int, input().split())
rp, cp = map(int, input().split())
f = [input().split() for i in range(n)]

d = {
	"U":(-1, 0),
	"D":(1, 0),
	"R":(0, 1),
	"L":(0, -1)
}

def game(start):
	t = False
	y, x = start
	r = {(y, x)}
	while True:
		word = f[y-1][x-1]
		count, command = int(word[:-1]), word[-1]
		while count > 0:
			iy, ix = d[command]
			ny = y + iy
			nx = x + ix
			if ny > n:
				ny = 1
			if ny < 1:
				ny = n
			if nx > n:
				nx = 1
			if nx < 1:
				nx = n
			if (ny, nx) not in r:
				r.add((ny, nx))
				y, x = ny, nx
			else:
				t = True
				break
			count -= 1
		if t:
			break
	return len(r)
g_score = game((rg,cg))
p_score = game((rp,cp))
if g_score > p_score:
	print(f"goorm {g_score}")
else:
	print(f"player {p_score}")


# 최적화된 코드
n = int(input())
rg, cg = map(int, input().split())
rp, cp = map(int, input().split())
f = [input().split() for i in range(n)]

directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "R": (0, 1),
    "L": (0, -1)
}

def new_position(y, x, command):
    dy, dx = directions[command]
    y += dy
    x += dx
    return (y - 1) % n + 1, (x - 1) % n + 1

def game(start):
    y, x = start
    visited = {(y, x)}
    revisited = False

    while not revisited:
        word = f[y-1][x-1]
        count, command = int(word[:-1]), word[-1]

        for _ in range(count):
            y, x = new_position(y, x, command)
            if (y, x) in visited:
                revisited = True
                break
            visited.add((y, x))

    return len(visited)

g_score = game((rg,cg))
p_score = game((rp,cp))

if g_score > p_score:
    print(f"goorm {g_score}")
else:
    print(f"player {p_score}")
	
# 3
# 1 1
# 3 3
# 1L 2L 1D
# 2U 3R 1D
# 2R 2R 1U

# goorm 4

# 4
# 4 2
# 2 4
# 1L 3D 3L 1U
# 2D 2L 4U 1U
# 2D 2L 4U 3L
# 4D 4D 1R 4R

# player 6