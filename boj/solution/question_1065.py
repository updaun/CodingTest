def hansu(n):
    num_list = []
    for i in range(1, n+1):
        if i < 100:
            num_list.append(i)
        else:
            if int(str(i)[0]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[2]):
                num_list.append(i)
    return len(num_list)

n = int(input())

print(hansu(n))
