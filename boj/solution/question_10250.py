n = int(input())
checkin_list = []
for i in range(n):
    checkin_list.append(list(map(int, input().split(" "))))

for i in checkin_list:
    H, W, P = i
    if P%H != 0:
        if P//H == 1:
            print(str(P%H)+"0"+"1")
        elif P//H < 10:
            print(str(P%H)+"0"+str(P//H+1))
        else:
            print(str(P%H)+str(P//H+1))
    else:
        if P//H == 1:
            print(str(P%H)+"0"+"1")
        if P//H < 10:
            print("1"+"0"+str(P//H+1))
        else:
            print("1"+str(P//H+1))
