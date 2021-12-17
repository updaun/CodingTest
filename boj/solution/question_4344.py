n = int(input())
number_list = []
for i in range(n):
    number_list.append(list(map(int, input().split())))

for list in number_list:
    student_cnt = list[0]
    student_score = list[1:]
    score_mean = sum(student_score)/student_cnt
    result = round(len([i for i in student_score if i> score_mean]) / student_cnt * 100, 3)
    print(f'{result:.3f}%')