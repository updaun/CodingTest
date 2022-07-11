import sys
input = sys.stdin.readline
drawf = []
for i in range(9):
    drawf.append(int(input()))
target = sum(drawf)-100
for i in drawf:
    for j in drawf:
        if i != j:
            if i+j == target:
                drawf.remove(i)
                drawf.remove(j)
print("\n".join(map(str, drawf)))