a, b, c = sorted(list(map(int, input().split())))
if b-a == c-b:
    print(c+(b-a))
else:
    if b-a > c-b:
        print(a+(c-b))
    else:
        print(b+(b-a))
