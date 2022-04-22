import sys
n = int(sys.stdin.readline())

def cal_gcd(n, m):
    if m == 0:
        return n
    else:
        return cal_gcd(m, n%m)
n_list = []
for i in range(n):
    n_list.append(int(sys.stdin.readline()))
n_list.sort()
n_list = [n_list[i+1]-n_list[i] for i in range(len(n_list)-1)]
gcd = n_list[0]
for i in range(1, n-1):
    gcd = cal_gcd(gcd, n_list[i])
divs = []
for i in range(1, int(gcd**0.5)+1):
    if gcd%i == 0:
        divs.append(i)
        if i != gcd//i:
            divs.append(gcd//i)
if 1 in divs:
    divs.remove(1)
divs.sort()
print(" ".join(map(str, divs)))
