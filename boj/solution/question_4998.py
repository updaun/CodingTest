while True:
    try:
        input_str = input()
        if input_str:
            n, b, m = map(float, input_str.split())
            year = 0
            while n < m:
                n += (n/100)*b
                year += 1 
            print(year)
    except EOFError:
        break
