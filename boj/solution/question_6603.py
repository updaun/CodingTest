import sys
input = sys.stdin.readline

def back_tracking(arr):

    if len(arr) == 7:
        print(" ".join(map(str, arr[1:])))
        return

    for i in range(len(l)):
        if l[i] not in arr and arr[-1] < l[i]:
            arr.append(l[i])
            back_tracking(arr)
            arr.pop()

while True:

    n_list = list(map(int, input().split()))

    if n_list == [0]:
        break

    n = n_list[0]
    l = n_list[1:]

    back_tracking([0])
    print()