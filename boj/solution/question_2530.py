import sys
h,m,s = list(map(int, sys.stdin.readline().split()))
second = int(sys.stdin.readline())
temp = (h*60*60) + (m*60) + s + second
H = temp // 3600
temp = temp - (H*3600)
M = temp // 60
temp = temp - (M*60)
S = temp
while H >= 24:
    H -= 24
while M >= 60:
    M -= 60
while S >= 60:
    S -= 60
print(H,M,S)

'''
# 다른 사람의 깔끔한 풀이

h,m,s = map(int,input().split())
t = int(input())

s += t
m += s//60
h += m//60
print(h%24,m%60,s%60)
'''