dial = {
    2 : ["A","B","C"],
    3 : ["D","E","F"],
    4 : ["G","H","I"],
    5 : ["J","K","L"],
    6 : ["M","N","O"],
    7 : ["P","Q","R","S"],
    8 : ["T","U","V"],
    9 : ["W","X","Y","Z"],
}
s = input()
result = 0
for i in s:
    for v in dial.values():
        if i in v:
            result += (list(dial.values()).index(v) + 3)
print(result)