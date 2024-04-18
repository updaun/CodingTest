# https://programmers.co.kr/learn/courses/30/lessons/92334
 
# 코딩테스트 연습
# 2022 KAKAO BLIND RECRUITMENT
# 신고 결과 받기

def solution(id_list, report, k):
    answer = []
    ban = dict()
    report_dict = dict()
    ban_list = []
    
    # 누가 누구를 신고했는지 체크하기 위한 딕셔너리 초기화
    for i in id_list:
        report_dict[i] = []

    # 신고 횟수 확인을 위한 딕셔너리 생성
    for i in set(report):
        user_id, report_id = i.split()
        if report_id not in ban.keys():
            ban[report_id] = 1
        else:
            ban[report_id] += 1
        # 누가 누구는 신고했는지 딕셔너리에 저장
        if user_id in report_dict.keys():
            report_dict[user_id].append(report_id)
            
    # k와 비교하여 정지된 아이디 정리
    for i in ban.keys():
        if ban[i] >= k:
            ban_list.append(i)

    # 집합을 활용하여 정지된 아이디와 교집합        
    for id in id_list:
        answer.append(len(set(report_dict[id]).intersection(set(ban_list))))
        
    return answer