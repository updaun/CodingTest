result = 0
n = 0
score = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}
while True:
    try:
        subject, c, s  = input().split()
        if s != "P":
            result += int(c[0]) * score[s]
            n += int(c[0])
    except EOFError:
        break
print(f"{result / n:.6f}")
