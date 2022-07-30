import sys
input = sys.stdin.readline
parts = {
    0:350.34,
    1:230.90,
    2:190.55,
    3:125.30,
    4:180.90,
}
for i in range(int(input())):
    result = 0
    for idx, count in enumerate(list(map(int, input().split()))):
        result += parts[idx]*count
    print(f'${result:.2f}')