# a, b = map(int, input().split())
# print(a + b)
# print(a - b)
# print(a * b)
# print(a // b)
# print(a % b)


# a, b, c = map(int, input().split())
# print((a + b) % c)
# print(((a % c) + (b % c)) % c)
# print((a * b) % c)
# print(((a % c)*(b%c)) % c)

# a = int(input())
# b = int(input())

# b_100 = b // 100
# b_10 = (b - (b_100*100))//10
# b_1 = b - (b_100*100) - (b_10*10)

# print(a * b_1)
# print(a * b_10)
# print(a * b_100)
# print(a * b)

# a, b = map(int, input().split())

# if a - b < 0: print("<")
# elif a - b > 0: print(">")
# else: print("==")

# a = int(input())

# if a >= 90: print("A")
# elif a>= 80: print("B")
# elif a>= 70: print("C")
# elif a>= 60: print("D")
# else: print("F")

# boj 2753번 윤년
# n = int(input())
# if n % 400 == 0:
#     print(1)
# elif (n % 4 == 0) and (n % 100 != 0):
#     print(1)
# else:
#     print(0)

# boj 14681번 사분면 고르기
# x = int(input())
# y = int(input())
# if x > 0 and y > 0 : print(1)
# elif x < 0 and y > 0 : print(2)
# elif x < 0 and y < 0 : print(3)
# else: print(4)

# boj 2884번 알람 시계
# h, m = map(int, input().split())
# s = 45
# if m - s < 0:
#     h -= 1
#     m += 15
#     if m > 59:
#         m -= 60
#         h += 1
# else:
#     m = m - s

# if h > 23: h -= 24
# elif h < 0: h = 23
# print(h, m)

# boj 2739번 구구단 
# n = int(input())
# for i in range(1, 10):
#     print(f'{n} * {i} = {n*i}')

# boj 10950번 A+B -3

# n = int(input())

# for i in range(n):
#     a,b = map(int, input().split())
#     print(a+b)

