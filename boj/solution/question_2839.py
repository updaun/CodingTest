# n = int(input())
# cnt = 0
# while n >= 5:
#     n -= 5
#     cnt += 1
# if n == 1:
#     if cnt == 0:
#         print(-1)
#     else:
#         cnt += 1
#         print(cnt)
# elif n == 2:
#     if cnt > 1:
#         cnt += 2
#         print(cnt)
#     else:
#         print(-1)
# elif n == 3:
#     cnt += 1
#     print(cnt)
# elif n == 4:
#     if cnt == 0:
#         print(-1)
#     else:
#         cnt += 2
#         print(cnt)
# else:
#     print(cnt)
sugar = int(input())
bag = 0
while sugar >= 0:
    if sugar % 5 == 0:
        bag += (sugar // 5)
        print(bag)
        break
    sugar -= 3
    bag += 1
else:
    print(-1)