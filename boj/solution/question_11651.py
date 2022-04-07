n = int(input())
coordinate_list = []
for i in range(n):
    coordinate_list.append(list(map(int, input().split())))
result = sorted(coordinate_list, key = lambda x:(x[1],x[0]))
for a,b in result:
    print(a,b)