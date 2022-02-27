n = int(input())
total_list = []
for i in range(n):
    s = input()
    total_list.append(s)
result = 0
for s in total_list:
    s_list = [s[0]]
    triger = True
    for i in range(1, len(s)-1):
        if s[i] != s[i-1] and s[i] not in s_list:
            s_list.append(s[i])
        elif s[i] != s[i-1] and s[i] in s_list:
            triger = False
            continue
        if s[-1] != s[-2] and s[-1] in s_list:
            triger = False
    result += int(triger)
print(result)