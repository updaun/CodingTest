while True:
    try:
        count = 0
        n, m = map(int, input().split())
        for i in range(n, m+1):
            if len(str(i)) == len(set([a for a in str(i)])):
                count += 1
        print(count)
    except EOFError:
        break