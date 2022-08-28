import sys
input = sys.stdin.readline
while True:
    input_str = input().rstrip()
    if input_str == "0":
        break
    input_list = list(map(int, input_str.split()))
    n = input_list[0]
    result = [input_list[1]]
    if n >= 2:
        for i in range(2, n+1):
            if input_list[i-1] != input_list[i]:
                result.append(input_list[i])
    print(" ".join(map(str, result))+" $")