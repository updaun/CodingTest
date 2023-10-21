import sys

input = sys.stdin.readline

while True:
    string = input().rstrip()
    if string == '.':
        break
    stack = []
    flag = True
    for c in string:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            if not stack or stack[-1] == '[':
                flag = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif c == ']':
            if not stack or stack[-1] == '(':
                flag = False
                break
            elif stack[-1] == '[':
                stack.pop()
    if stack:
        flag = False
    print('yes' if flag else 'no')