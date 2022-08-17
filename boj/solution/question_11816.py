num_str = input()
if num_str[:2] == "0x":
    print(int(num_str, 16))
elif num_str[0] == "0":
    print(int(num_str, 8))
else:
    print(num_str)
