import sys
input = sys.stdin.readline
multiple_num = int(input())
while True:
    input_num = int(input())
    if input_num == 0:
        break
    if input_num % multiple_num == 0:
        print(f'{input_num} is a multiple of {multiple_num}.')
    else:
        print(f'{input_num} is NOT a multiple of {multiple_num}.')