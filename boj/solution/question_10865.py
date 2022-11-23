# 리스트를 활용한 풀이
# 메모리 31552KB, 시간 968ms
import sys
n,m=map(int,sys.stdin.readline().split())
cnt=[0]*(n+1)
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    cnt[a]+=1
    cnt[b]+=1
for i in range(1,n+1):
    print(cnt[i])

# 딕셔너리를 활용한 풀이
# 메모리 118392KB, 시간 1556ms
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
student = dict()
for i in range(n):
    student[i+1] = []
for i in range(m):
    a, b = map(int, input().split())
    student[a].append(b)
    student[b].append(a)
for i in range(1, n+1):
    print(len(student[i]))