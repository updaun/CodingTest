import sys
input = sys.stdin.readline
def gcd(d):
    divs = []
    for i in range(1, int(d**0.5)+1):
        if d%i == 0:
            divs.append(i)
            if i != d//i:
                divs.append(d//i)
    return divs
n = int(input())
num_list = list(map(int, input().split()))
result = set(gcd(num_list[0]))
for i in range(1, n):
    result = result.intersection(set(gcd(num_list[i])))
print("\n".join(map(str, sorted(result))))