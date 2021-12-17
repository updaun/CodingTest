n = int(input())
quiz_list = []
for i in range(n):
    quiz_list.append(input())

for quiz in quiz_list:
    score = 0
    combo = 1
    for i in range(len(quiz)):
        if quiz[i] == "O":
            score += combo
            combo += 1
        else:
            combo = 1
    print(score)