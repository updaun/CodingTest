import sys
input = sys.stdin.readline
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A_score = 0
B_score = 0
last_winner = ''
for i in range(10):
    if A[i] > B[i]:
        A_score += 3
        last_winner = 'A'
    elif A[i] < B[i]:
        B_score += 3
        last_winner = 'B'
    else:
        A_score += 1
        B_score += 1
print(A_score, B_score)
if A_score > B_score:
    print('A')
elif A_score < B_score:
    print('B')
else:
    if last_winner == '':
        print('D')
    else:
        print(last_winner)