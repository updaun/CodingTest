import sys
input = sys.stdin.readline
t = int(input())
d = {
    1 : "Yakk",
    2 : "Doh",
    3 : "Seh",
    4 : "Ghar",
    5 : "Bang",
    6 : "Sheesh"
}
ds = {
    1 : "Habb Yakk",
    2 : "Dobara", 
    3 : "Dousa",
    4 : "Dorgy",
    5 : "Dabash",
    6 : "Dosh"
}
for i in range(t):
    a,b = sorted(list(map(int, input().split())))
    result = f'Case {i+1}: '
    if a == b:
        result += ds[a]
    else:
        if a == 5 and b == 6:
            result += "Sheesh Beesh"
        else:
            result += f"{d[b]} {d[a]}"
    print(result)
            