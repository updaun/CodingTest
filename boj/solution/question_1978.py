n = int(input())
target_list = list(map(int, input().split(" ")))
cnt = 0
for num in target_list:
    flag = False
    div = 2
    if num == 1:
        continue
    while num > div:
        if num % div == 0:
            flag = True
            break
        div += 1
    if flag == False:
        cnt += 1
print(cnt)