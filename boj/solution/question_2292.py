x = int(input())
cnt = 0 
while x > 0:
    if cnt == 0:
        x -= 1
    else:
        x -= 6*cnt 
    cnt += 1
print(cnt)