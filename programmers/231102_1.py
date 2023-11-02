# 프로그래머스
# 프로그래밍 강의 > PCCE 모의고사 > [PCCE 모의고사] 10번
# https://school.programmers.co.kr/learn/courses/19275/lessons/240615

def solution(snippet, message):
    answer = []
    snippets = { k: v for k, v in snippet}
    m_list = message.split(" ")
    for m in m_list:
        if m in snippets.keys():
            answer.append(snippets[m])
        else:
            answer.append(m)
    return " ".join(answer)

q = solution([["IMO,", "In my opinion,"], ["AYS?", "Are you serious?"], ["TTYL.", "Talk to you later."]], "IMO, it does not look so good. AYS? TTYL.")
assert q == "In my opinion, it does not look so good. Are you serious? Talk to you later.", "불일치"
print(q)

q = solution([["msg", "message"], ["m", "me"], ["s", "see"], ["g", "group"]], "msg")
assert q == "message", "불일치"
print(q)

q = solution([["IMO", "In my opinion"]], "IMO, IMO")
assert q == "IMO, In my opinion", "불일치"
print(q)



