n, m = tuple(map(int, input().split()))

n_list = []
result = []

def n_search():
    if len(n_list) == m:
        if sorted(n_list) not in result:
            result.append(sorted(n_list))
            print(" ".join(map(str, n_list)))
        return
    for i in range(1, n+1):
        if i in n_list:
            continue
        n_list.append(i)
        n_search()
        n_list.pop()
n_search()