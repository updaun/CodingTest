import sys
for i in range(3):
    sh,sm,ss,fh,fm,fs = map(int, sys.stdin.readline().split())
    temp = (3600*fh +60*fm +fs) - (3600*sh +60*sm +ss)
    th, temp = divmod(temp, 3600)
    tm, ts = divmod(temp, 60)
    print(th, tm, ts)
    