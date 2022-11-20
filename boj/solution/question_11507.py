s = input()
cards = {"P":[0]+[1]*13, "K":[0]+[1]*13, "H":[0]+[1]*13, "T":[0]+[1]*13}
for i in range(0, len(s), 3):
    temp = cards[s[i]][int(s[i+1:i+3])]
    if temp == 1:
        cards[s[i]][int(s[i+1:i+3])] = 0
    else:
        print("GRESKA")
        break
else:
    print(sum(cards["P"]), sum(cards["K"]), sum(cards["H"]), sum(cards["T"]))
    