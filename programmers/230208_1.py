# 프로그래머스
# 코딩테스트 연습 > 힙(Heap) > 더 맵게

# 시간초과
from collections import Counter
def solution(X, Y):
    answer = ''
    cx = Counter(list(X))
    cy = Counter(list(Y))
    result = []
    for i in cx.keys():
        if i in cy.keys():
            result.append(i)
    if len(result) == 0:
        return "-1"
    for s in sorted(result, reverse=True):
        answer += s*min(cx[s], cy[s])
    # 시간 초과의 원인! 형변환은 생각보다 시간이 오래 걸린다.
    if int(answer) == 0:
        return "0"
    return answer

# 개선 코드
from collections import Counter
def solution(X, Y):
    answer = ''
    cx = Counter(list(X))
    cy = Counter(list(Y))
    result = []
    for i in cx.keys():
        if i in cy.keys():
            result.append(i)
    if len(result) == 0:
        return "-1"
    for s in sorted(result, reverse=True):
        answer += s*min(cx[s], cy[s])
    if len(result) == 1 and result[0] == "0":
        return "0"
    return answer

print(solution("100", "2345")) # "-1"
print(solution("100", "203045")) # "0"
print(solution("100", "123450")) # "10"
print(solution("12321", "42531")) # "321"
print(solution("5525", "1255")) # "552"
