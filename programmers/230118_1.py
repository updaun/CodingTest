# 프로그래머스
# 코딩테스트 연습 > 2018 KAKAO BLIND RECRUITMENT > [1차] 뉴스 클러스터링

def solution(str1, str2):
    a = []
    b = []
    inter = []
    for i in range(len(str1)-1):
        temp = str1[i:i+2]
        if temp.isalpha():
            a.append(temp.lower())
    for i in range(len(str2)-1):
        temp = str2[i:i+2]
        if temp.isalpha():
            b.append(temp.lower())
    if len(a) < len(b):
        temp_a = b.copy()
        temp_b = a.copy()
    else:
        temp_a = a.copy()
        temp_b = b.copy()
    for i in temp_a:
        if i in temp_b:
            inter.append(i)
            temp_b.remove(i)
    if (len(a) + len(b) - len(inter)) <= 0:
        return 65536
    return int(len(inter) / (len(a) + len(b) - len(inter)) * 65536)
    
print(solution("FRANCE", "french")) # 16384
print(solution("handshake", "shake hands")) # 65536
print(solution("aa1+aa2", "AAAA12")) # 43690
print(solution("E=M*C^2", "e=m*c^2")) # 65536