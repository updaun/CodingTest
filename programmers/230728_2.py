# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 대충 만든 자판
# https://school.programmers.co.kr/learn/courses/30/lessons/160586

def solution(keymap, targets):
    answer = []
    for target in targets:
        temp = 0
        for s in target:
            touch = [i.index(s)+1 for i in keymap if s in i]
            if len(touch) == 0:
                answer.append(-1)
                break
            else:
                touch = min(touch)
                temp += touch
        if touch:
            answer.append(temp)
    return answer

# 다른 사람의 풀이 - 키 배열을 미리 만들어놓고, 인덱스를 활용
def solution(keymap, targets):
    answer = []
    #최솟값 저장
    alpha = [101 for i in range(26)]
    for i in keymap:
        for idx, j in enumerate(i):
            k = ord(j)-ord('A')
            alpha[k] = min(alpha[k],idx+1)

    for i in targets:
        total = 0
        for j in i:
            cnt = alpha[ord(j) - ord('A')]
            if cnt ==101:
                answer.append(-1)
                break
            else:
                total+= cnt
        else:
            answer.append(total)
    return answer


q = solution(["ABACD", "BCEFD"], ["ABCD","AABB"])
assert q == [9, 4], "불일치"
print(q)

q = solution(["AA"], ["B"])
assert q == [-1], "불일치"
print(q)

q = solution(["AGZ", "BSSS"], ["ASA","BGZ"])
assert q == [4, 6], "불일치"
print(q)