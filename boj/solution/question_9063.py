n = int(input())
x_list = []
y_list = []
for i in range(n):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)
x_min, x_max = min(x_list), max(x_list)
y_min, y_max = min(y_list), max(y_list)
print((x_max-x_min)*(y_max-y_min))
