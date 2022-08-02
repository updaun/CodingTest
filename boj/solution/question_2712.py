import sys
input = sys.stdin.readline
for i in range(int(input())):
    value, unit = input().split()
    if unit == 'kg':
        value = float(value)*2.2046
        unit = 'lb'
    elif unit == 'l':
        value = float(value)*0.2642
        unit = 'g'
    elif unit == 'lb':
        value = float(value)*0.4536
        unit = 'kg'
    else:
        value = float(value)*3.7854
        unit = 'l'
    print(f"{value:.4f} {unit}")