a = int(input())
b = int(input())
c = int(input())

multiply_number = str(a*b*c)
number_list = []
for i in range(len(multiply_number)):
    number_list.append(multiply_number[i])
for i in range(10):
    print(number_list.count(str(i)))