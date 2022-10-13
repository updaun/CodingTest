n = int(input())

def check(num):
    n_list = ["4", "7"]
    result = 0
    temp = str(num)
    for i in n_list:
        result += temp.count(i)
    return len(temp) == result

while True:
    if check(n):
        print(n)
        break
    n -= 1