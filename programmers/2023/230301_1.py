# 프로그래머스
# 코딩테스트 연습 > 2019 KAKAO BLIND RECRUITMENT > 오픈채팅방
# https://school.programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    mapping = dict()
    for r in record:
        r_list = r.split()
        if r_list[0] in ["Enter", "Change"]:
            mapping[r_list[1]] = r_list[2]
    
    for i in record:
        r_list = i.split()
        if r_list[0] == "Enter":
            answer.append(f"{mapping[r_list[1]]}님이 들어왔습니다.")
        elif r_list[0] == "Leave":
            answer.append(f"{mapping[r_list[1]]}님이 나갔습니다.")
    
    return answer


q = solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])
assert q == ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.",
             "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."], "불일치"
print(q)
