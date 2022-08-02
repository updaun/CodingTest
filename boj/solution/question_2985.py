import sys
input = sys.stdin.readline
a,b,c = map(int, input().split())
oper = ['+', '-', '*', '/']
ab = [a+b, a-b, a*b, int(a/b)]
bc = [b+c, b-c, b*c, int(b/c)]
if c in ab:
    print(f'{a}{oper[ab.index(c)]}{b}={c}')
elif a in bc:
    print(f'{a}={b}{oper[bc.index(a)]}{c}')
