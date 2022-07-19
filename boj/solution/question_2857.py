import sys
input = sys.stdin.readline
FBI = []
for i in range(1, 6):
    if 'FBI' in input().rstrip():
        FBI.append(i)
if len(FBI) == 0:
    print("HE GOT AWAY!")
else:
    print(" ".join(map(str, FBI)))