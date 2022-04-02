h, w = tuple(map(int, input().split()))
chess = []
for i in range(h):
    chess.append([int(i=="W") for i in input()])

answer1 = []
answer2 = []
cross = 0
for i in range(8):
    answer1.append([int(i%2==cross) for i in range(8)])
    answer2.append([int(i%2!=cross) for i in range(8)])
    if cross == 0: cross = 1
    elif cross == 1: cross = 0

result = []

for h_shift in range(h-7):
    sub_chess = chess[h_shift:h_shift+8]
    for w_shift in range(w-7):
        paint1 = 0
        paint2 = 0
        answer_h = 0
        for sub in sub_chess:
            for order in range(8):
                if sub[w_shift+order] != answer1[answer_h][order]:
                    paint1 += 1
                elif sub[w_shift+order] != answer2[answer_h][order]:
                    paint2 += 1
            answer_h += 1
        result.append(paint1)
        result.append(paint2)
print(min(result))  