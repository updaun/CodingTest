m, n = map(int, input().split())

table = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "0":"zero",
}

def change(number):
    n_str = str(number)
    return " ".join(map(str, [table[i] for i in n_str]))

result = sorted(list(range(m, n+1)), key=lambda x:change(x))
for i in range(0, len(result), 10):
    try:
        print(*result[i:i+10])
    except:
        print(*result[i:])