import sys
input = sys.stdin.readline
for i in range(int(input())):
    sentence = input().split()
    sentence = sentence[2:]+sentence[:2]
    print(" ".join(map(str, sentence)))