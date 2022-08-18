import sys
input = sys.stdin.readline
science = []
history = []
for i in range(4):
    science.append(int(input()))
for i in range(2):
    history.append(int(input()))
print(sum(sorted(science, reverse=True)[:3]) + max(history))
