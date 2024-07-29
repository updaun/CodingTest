# 프로그래머스
# 코딩테스트 연습 > 2022 KAKAO TECH INTERNSHIP > 성격 유형 검사하기
# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    answer = ''
    t_dict = {
        "R":0,
        "T":0,
        "C":0,
        "F":0,
        "J":0,
        "M":0,
        "A":0,
        "N":0,
    }
    for q, c in zip(survey, choices):
        temp = c - 4
        if temp == 0:
            continue
        if temp < 0:
            t_dict[q[0]] += -temp
        else:
            t_dict[q[1]] += temp
    answer += "RT"[int(t_dict["R"] < t_dict["T"])] 
    answer += "CF"[int(t_dict["C"] < t_dict["F"])] 
    answer += "JM"[int(t_dict["J"] < t_dict["M"])] 
    answer += "AN"[int(t_dict["A"] < t_dict["N"])]
    return answer


q = solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])
assert q == "TCMA", "불일치"
print(q)

q = solution(["TR", "RT", "TR"], [7, 1, 3])
assert q == "RCJA", "불일치"
print(q)
