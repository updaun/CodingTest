n, m = tuple(map(int, input().split()))

n_list = []

def n_search():
    if len(n_list) == m:
        print(" ".join(map(str, n_list)))
        return
    for i in range(1, n+1):
        if len(n_list) != 0:
            if i < max(n_list):
                continue
        n_list.append(i)
        n_search()
        n_list.pop()

n_search()