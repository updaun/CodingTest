c = input()
table = {"1":True, "2":False, "3":False}
for t in c:
    if t == "A":
        table["1"], table["2"] = table["2"], table["1"] 
    elif t == "B":
        table["2"], table["3"] = table["3"], table["2"] 
    else:
        table["1"], table["3"] = table["3"], table["1"] 
print(*[k for k,v in table.items() if v==True])
