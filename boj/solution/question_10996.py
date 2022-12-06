n = int(input())
if n == 1:
    print("*")
else:
    for i in range(n*2):
        result = ""
        if i % 2 == 0:
            trigger = True
        else:
            trigger = False
        for j in range(n):
            if trigger:
                result += "*"
            else:
                result += " "
            trigger = not trigger
        print(result.rstrip())