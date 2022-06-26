# https://programmers.co.kr/learn/courses/30/lessons/72410

# 코딩테스트 연습
# 2021 KAKAO BLIND RECRUITMENT
# 신규 아이디 추천

def solution(new_id):
    process = new_id.lower()
    temp = ''
    for s in process:
        if s.isalpha() or s.isdigit() or s in ['-', '_', '.']:
            temp += s
    process = temp
    while '..' in process:
        process = process.replace('..', '.')
    if len(process) != 0:
        if process[0] == '.':
            process = process[1:]
    if len(process) != 0:
        if process[-1] == '.':
            process = process[:-1]
    else:
        process = 'a'
        
    if len(process) >= 16:
        process = process[:15]
    if len(process) != 0:
        if process[-1] == '.':
            process = process[:-1]
    if len(process) != 0:
        while len(process) < 3:
            process += process[-1]
    answer = process
    return answer