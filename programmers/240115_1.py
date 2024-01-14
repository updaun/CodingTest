# 프로그래머스
# 프로그래밍 강의 > PCCE 기출문제 > [PCCE 기출문제] 9번 / 이웃한 칸
# https://school.programmers.co.kr/learn/courses/30/lessons/250121

def solution(data, ext, val_ext, sort_by):
    index = ["code", "date", "maximum", "remain"]
    target = index.index(ext)
    sort_target = index.index(sort_by)
    c_data = [d for d in data if d[target] < val_ext]
    answer = sorted(c_data, key=lambda x:x[sort_target])
    return answer

q = solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]], "date", 20300501, "remain")
assert q == [[3,20300401,10,8],[1,20300104,100,80]], "불일치"
print(q)
