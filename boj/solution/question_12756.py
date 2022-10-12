import sys
input = sys.stdin.readline
a_attack, a_life = map(int, input().split())
b_attack, b_life = map(int, input().split())
a_time, a_remain = divmod(a_life, b_attack)
b_time, b_remain = divmod(b_life, a_attack)
if a_time == b_time:
    if a_remain == 0 and b_remain != 0:
        print("PLAYER B")
    elif a_remain != 0 and b_remain == 0:
        print("PLAYER A")
    else:
        print("DRAW")
else:
    if a_time > b_time:
        print("PLAYER A")
    else:
        print("PLAYER B")
    