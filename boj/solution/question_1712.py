A,B,C = tuple(map(int, input().split(" ")))
if B != C:
    b_line = int(A/(C-B))
    if b_line < 0:
        print(-1)
    else:
        print(b_line+1)
else:
    print(-1)