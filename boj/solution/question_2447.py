def star(n, x):
    output = []
    if n == 3:
        return x
    else:
        for i in x:
            output.append(i*3)
        for i in x:
            output.append(i+" "*len(x)+i)
        for i in x:
            output.append(i*3)
    return star(n//3, output)

n = int(input())
start = ["***", "* *", "***"]
result = star(n, start)
for i in result:
    print(i)
