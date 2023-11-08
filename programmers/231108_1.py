# 프로그래머스
# 프로그래밍 강의 > PCCE 기출문제 > [PCCE 기출문제] 10번
# https://school.programmers.co.kr/learn/courses/19274/lessons/240605

def solution(data, ext, val_ext, sort_by):
    col = ["code", "date", "maximum", "remain"]
    ext_index = col.index(ext)
    sort_index = col.index(sort_by)
    answer = []
    for d in data:
        if d[ext_index] > val_ext:
            continue
        answer.append(d)
    return sorted(answer, key=lambda x:x[sort_index])

q = solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]], "date", 20300501, "remain")
assert q == [[3,20300401,10,8],[1,20300104,100,80]], "불일치"
print(q)

