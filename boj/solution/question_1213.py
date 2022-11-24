import sys
from collections import deque
input = sys.stdin.readline
word = deque(sorted(input().rstrip()))
pre = ""
post = ""
temp = ""
while word:
    if word.count(word[0])%2 == 1:
        while word.count(word[0]) != 1:
            pre += word.popleft()
            if word:
                post = word.popleft() + post
        temp += word.popleft()
    else:
        pre += word.popleft()
        if word:
            post = word.popleft() + post
result = pre + temp + post
if result == result[::-1]:
    print(result)
else:
    print("I'm Sorry Hansoo")