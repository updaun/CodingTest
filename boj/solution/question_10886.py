import sys
n = int(sys.stdin.readline())
vote = 0
for i in range(n):
    vote += int(sys.stdin.readline())
if vote > n/2:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")