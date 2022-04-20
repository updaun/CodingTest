import sys
n, m = tuple(map(int, sys.stdin.readline().split()))

n_div = n
m_div = m

div = 2
result = 1
while True:
    if n_div%div==0 and m_div%div ==0:
        result *=div
        n_div /= div
        m_div /= div
        div = 2
    elif min(n_div, m_div) <= div:
        break
    else:
        div +=1
print(result)
print(int(result*n_div*m_div))