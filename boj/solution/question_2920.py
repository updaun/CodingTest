import sys
input = sys.stdin.readline
input_mel = list(map(int, input().split()))
if input_mel == [i for i in range(1, 9)]:
    print('ascending')
elif input_mel == [8-i for i in range(8)]:
    print('descending')
else:
    print('mixed')
