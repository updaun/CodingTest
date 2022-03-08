n = int(input())
test_case = []
for i in range(n):
    k = int(input())
    n = int(input())
    test_case.append((k,n))

def sum_list(target_list):
    new_list =[]
    for i in range(1, len(target_list)+1):
        new_list.append(sum(target_list[:i]))
    return new_list

for i in test_case:
    k, n = i
    p = 0
    zero = [i for i in range(1, n+1)]
    for i in range(k-1):
        zero = sum_list(zero)
    print(sum(zero))