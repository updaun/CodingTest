import sys
input = sys.stdin.readline
input_str = input().rstrip()
happy = input_str.count(':-)')
sad = input_str.count(':-(')
if happy == 0 and sad == 0:
    print('none')
elif happy > sad:
    print('happy')
elif happy < sad:
    print('sad')
else:
    print('unsure')
