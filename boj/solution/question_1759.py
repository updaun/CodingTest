import sys
input = sys.stdin.readline

l, c = map(int, input().split())
a = sorted(input().split())
answer = []

def is_vowel(s):
    return s in ['a', 'e', 'i', 'o', 'u']

def dfs(cnt, idx):
    if cnt == l:
        count_v, count_c = 0, 0

        for i in range(l):
            if is_vowel(answer[i]):
                count_v += 1
            else:
                count_c += 1
        
        if count_v >= 1 and count_c >= 2:
            print("".join(answer))
        
        return
    
    for i in range(idx, c):
        answer.append(a[i])
        dfs(cnt+1, i+1)
        answer.pop()

dfs(0, 0)
