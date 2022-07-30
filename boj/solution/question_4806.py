result = 0
while True:
    try:
        input_str = input()
        if input_str:
            result += 1
    except EOFError:
        break
print(result)
