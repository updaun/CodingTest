import sys
input = sys.stdin.readline
temper = float(input())
while True:
    current_temper = float(input())
    if current_temper == 999:
        break
    print(f'{current_temper - temper:.2f}')
    temper = current_temper
