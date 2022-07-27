import sys
input = sys.stdin.readline
for i in range(int(input())):
    question = input().rstrip()
    if '+' in question:
        a, b = map(int, question.split('+'))
        print(a+b)
    else:
        print('skipped')
