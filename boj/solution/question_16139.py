import sys
S = sys.stdin.readline().rstrip()
q = int(sys.stdin.readline())
for i in range(q):
    s, l, r = sys.stdin.readline().split()
    print(S[int(l):int(r)+1].count(s))