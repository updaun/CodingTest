import sys
input = sys.stdin.readline
score_table = [
    {"A":9.23076, "B":26.7, "C":1.835, "K":"T"},
    {"A":1.84523, "B":75, "C":1.348, "K":"F"},
    {"A":56.0211, "B":1.5, "C":1.05, "K":"F"},
    {"A":4.99087, "B":42.5, "C":1.81, "K":"T"},
    {"A":0.188807, "B":210, "C":1.41, "K":"F"},
    {"A":15.9803, "B":3.8, "C":1.04, "K":"F"},
    {"A":0.11193, "B":254, "C":1.88, "K":"T"},
]
for i in range(int(input())):
    p = list(map(int, input().split()))
    score = 0
    for i in range(7):
        if score_table[i]["K"] == "T":
            score += int(score_table[i]["A"] * (score_table[i]["B"] - p[i])**score_table[i]["C"])
        else:
            score += int(score_table[i]["A"] * (p[i] - score_table[i]["B"])**score_table[i]["C"])
    print(score)
