import sys
input = sys.stdin.readline
k = int(input())
for t in range(k):
    n = int(input())
    if n > 1:
        print("#"*n)
        for i in range(n-2):
            print("#"+"J"*(n-2)+"#")
        print("#"*n)
    else:
        print("#")
    print()