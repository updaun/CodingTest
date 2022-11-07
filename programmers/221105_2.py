# 2022 Winter Coding - 겨울방학 스타트업 인턴 프로그램
# 6
# 1 ~ 6번
# 1 2 3 | 4 5 6
# 학생번호 점수가 입력
# 3번 5점
# 점수가 같을 때는 낮은 번호의 학생이 우반에 간다.
# 우반(잘하는애들), 열반(못하는애들)
# 3 1 2 | 4 5 6
# 1 2 3 | 4 5 6
# 카운트 기준은 우반과 열반의 인원이 변경된 횟수
def solution(n, student, point):
    temp = dict()
    answer = 0
    for i in range(n):
        temp[i+1] = 0
    t = [i+1 for i in range(n)]
    a = t[:n//2]

    for i in range(len(student)):
        k, v = student[i], point[i]
        temp[k] += v
        temp_list = sorted(temp, key=lambda x:(-temp[x], x))
        c = sorted(temp_list[:n//2])
        if a != c:
            answer += 1
            a = c
    return answer