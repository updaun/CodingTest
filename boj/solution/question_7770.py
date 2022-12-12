n = int(input())
n_list = [1]
temp = 1
pyramid = [1]
for i in range(1, 1145):
    temp += 4*i
    n_list.append(temp)
    pyramid.append(sum(n_list))
for i in range(len(pyramid)):
    if  pyramid[i] > n:
        print(i)
        break