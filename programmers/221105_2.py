# 2022 Winter Coding - 겨울방학 스타트업 인턴 프로그램
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