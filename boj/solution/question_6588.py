import sys
input = sys.stdin.readline

def is_prime_num(n):
    for i in range(2, int(n**0.5)+1): 
        if n % i == 0:
            return False
    return True

while True:
    num = int(input())
    if num == 0:
        break

    temp = 3
    try:
        while not is_prime_num(temp) or not is_prime_num(num - temp):
            temp += 1
    except EOFError:
        print("Goldbach's conjecture is wrong.")

    print(f"{num} = {temp} + {num-temp}")
        