import sys
c  = int(sys.stdin.readline())
n_list = []

for i in range(6):
    n_list.append(list(map(int, sys.stdin.readline().split())))

directions = [i[0] for i in n_list]
lengths = [i[1] for i in n_list]

updown_direction = []
leftright_direction = []
for i in n_list:
    if i[0] in (3,4) != 0:
        updown_direction.append(i[1])
    else:
        leftright_direction.append(i[1])

small_rect_index = lengths.index(max(updown_direction)) + 3
if small_rect_index > 5:
    small_rect_index -= 6
small_rect_index2 = lengths.index(max(leftright_direction)) + 3
if small_rect_index2 > 5:
    small_rect_index2 -= 6

print((max(updown_direction)*max(leftright_direction) - lengths[small_rect_index]*lengths[small_rect_index2])*c)