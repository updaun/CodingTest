import sys
n = int(sys.stdin.readline())
word_list = []
for i in range(n):
    word_list.append(str(sys.stdin.readline().strip()))
result = sorted(list(set(word_list)), key=lambda x:(len(x), x))
for i in result:
    print(i)