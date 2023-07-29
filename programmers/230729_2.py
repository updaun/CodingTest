# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 조건에 맞게 수열 변환하기 2
# https://school.programmers.co.kr/learn/courses/30/lessons/181881

def solution(strArr):
    l = [len(i) for i in strArr]
    s = set(l)
    return max([l.count(i) for i in s])

# 다른 사람의 풀이(형변환 없이)
def solution(strArr):
    a=[0]*31
    for x in strArr: a[len(x)]+=1
    return max(a)

q = solution(["a","bc","d","efg","hi"])
assert q == 2, "불일치"
print(q)

