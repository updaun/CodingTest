import sys
db = []
in_subway = 0
for i in range(4):
    out_p, in_p = list(map(int, sys.stdin.readline().split()))
    in_subway -= out_p
    in_subway += in_p
    db.append(in_subway)
print(max(db))