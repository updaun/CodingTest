import sys
input = sys.stdin.readline

for i in range(int(input())):
    word = input().rstrip()
    n = len(word)
    word = [word[i] for i in range(n)]
    for i in range(n-1, 0, -1):
        if ord(word[i-1]) < ord(word[i]):
            temp = i-1
            break
    else:
        print("".join(map(str, word)))
        continue

    for i in range(n-1, 0, -1):
        if ord(word[temp]) < ord(word[i]):
            word[temp], word[i] = word[i], word[temp]
            word = word[:temp+1]+sorted(word[temp+1:])
            print("".join(map(str, word)))
            break