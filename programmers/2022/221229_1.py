# 프로그래머스
# 코딩테스트 연습 > 2021 카카오 채용연계형 인턴십 > 숫자 문자열과 영단어

def solution(s):
    n_dict = {
        "zero":"0",
        "one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9",
    }
    for key in n_dict.keys():
        if key in s:
            s = s.replace(key, n_dict[key])
    return int(s)

print(solution("one4seveneight")) # 1478
print(solution("23four5six7")) # 234567
print(solution("2three45sixseven")) # 234567
print(solution("123")) # 123

from collections import deque
def solution(people, limit):
    answer = 0
    q = deque(sorted(people))
    while q:
        if len(q) == 1:
            answer += 1
            break
        if q[0] + q[-1] <= limit:
            q.popleft()
            q.pop()
        else:
            q.pop()
        answer += 1
    return answer