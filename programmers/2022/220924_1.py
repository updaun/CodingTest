# 코딩테스트
# 2023 KAKAO BLIND RECRUITMENT

def daytotime(day):
    y, m, d = map(int, day.split("."))
    return y*12*28+m*28+d

def solution(today, terms, privacies):
    answer = []
    today_timestamp=daytotime(today)
    terms_dict = {}
    for term in terms:
        k, v = term.split()
        terms_dict[k] = int(v)

    index = 1
    for privacie in privacies:
        day, t = privacie.split()
        day_timestamp = daytotime(day)
        if today_timestamp >= day_timestamp + (terms_dict[t]*28):
            answer.append(index)
        index += 1
    
    return answer