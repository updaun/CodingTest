n = int(input())
checkin_list = []
for i in range(n):
    checkin_list.append(list(map(int, input().split(" "))))
for i in checkin_list:
    H, W, P = i
    floor, room_num = 1, 1
    while P > 1:
        floor += 1
        if floor > H:
            floor = 1
            room_num += 1
        P -= 1
    if room_num < 10:
        print(str(floor)+"0"+str(room_num))
    else:
        print(str(floor)+str(room_num))