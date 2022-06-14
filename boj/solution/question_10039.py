import sys
result = 0
for i in range(5):
    score = int(sys.stdin.readline())
    if score > 40:
        result += score
    else:
        result += 40
print(int(result/5))