t = input()
while "()" in t:
    t = t.replace("()", "")
print(len(t))