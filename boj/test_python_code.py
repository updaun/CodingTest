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

a = int(input())

if a >= 90: print("A")
elif a>= 80: print("B")
elif a>= 70: print("C")
elif a>= 60: print("D")
else: print("F")

