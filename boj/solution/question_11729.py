def hanoi(n, start, sub, target):
    if n == 1:
        move.append([start, target])
        return None
    else:
        hanoi(n-1, start, target, sub)
        move.append([start, target])
        hanoi(n-1, sub, start, target)

move = []
n = int(input())
hanoi(n, 1, 2, 3)
print(len(move))
for i in move:
    print(i[0], i[1])