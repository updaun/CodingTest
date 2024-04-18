# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 세 개의 구분자
# https://school.programmers.co.kr/learn/courses/30/lessons/181862


def solution(myStr):
    split_list = ["a", "b", "c"]
    temp = ""
    result = []
    for i in myStr:
        if i not in split_list:
            temp += i
        else:
            if temp != "":
                result.append(temp)
            temp = ""
    if temp != "":
        result.append(temp)
    if len(result) == 0:
        return ["EMPTY"]
    return result

# 다른 사람의 풀이 (replace 활용)
def solution(myStr):
    s=myStr.replace('b','a')
    s=s.replace('c','a')
    s=s.split('a')
    answer=[]
    for x in s:
        if x: answer.append(x)
    if not answer:return ["EMPTY"]
    return answer

q = solution("baconlettucetomato")
assert q == ["onlettu", "etom", "to"], "불일치"
print(q)

q = solution("abcd")
assert q == ["d"], "불일치"
print(q)

q = solution("cabab")
assert q == ["EMPTY"], "불일치"
print(q)