import sys
n = int(sys.stdin.readline())
for i in range(n):
    idx, word = sys.stdin.readline().split()
    target = int(idx)-1
    print(word[:target]+word[target+1:])