import sys
input = sys.stdin.readline
r, c = map(int, input().split())
a, b = map(int, input().split())
result = []
row = ""
chess = True
chess_type = {
    True:"X",
    False:"."
}
for l in range(r):
    for i in range(a):
        chess = l % 2 == 0
        for _ in range(c):
            row += b * chess_type[chess]
            chess = not chess
        result.append(row)
        row = ""
print(*result, sep="\n")