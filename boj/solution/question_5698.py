import sys
input = sys.stdin.readline
while True:
    s = input().rstrip()
    if s == '*':
        break
    s_list = s.lower().split()
    print("Y" if len(set([w[0] for w in s_list])) == 1 else "N")