x_list = []
y_list = []
for i in range(3):
    x,y = tuple(map(int, input().split(" ")))
    x_list.append(x)
    y_list.append(y)
result_x = 0
result_y = 0
for x in x_list:
    if x_list.count(x) == 1:
        result_x = x
for y in y_list:
    if y_list.count(y) == 1:
        result_y = y
print(result_x, result_y)
