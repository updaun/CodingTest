def number_sum(n):
    str_n = str(n)
    sum_n = n
    for i in str_n:
        sum_n += int(i)
    return sum_n

test_number_list = [i+1 for i in range(10000)]
total_list = [i+1 for i in range(10000)]

for test_number in test_number_list:
    test_number = number_sum(test_number)
    if test_number in total_list:
        total_list.remove(test_number)
    if test_number > 10000:
        continue

for i in total_list:
    print(i)