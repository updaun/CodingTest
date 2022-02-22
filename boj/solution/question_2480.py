dice = sorted(list(map(int, input().split(" "))))
set_dice = set(dice)
if len(set_dice) == 1:
    print(dice[0]*1000 + 10000)
elif len(set_dice) == 2:
    print(dice[1]*100 + 1000)
elif len(set_dice) == 3:
    print(dice[-1]*100)