# 프로그래머스
# 코딩테스트 연습 > 2019 카카오 개발자 겨울 인턴십 > 튜플


def solution(s):
    answer = []
    temp_list = []
    temp = []
    temp_str = ""
    for idx, i in enumerate(s[1:-1]):
        if i == "{":
            temp = []
        elif i.isdigit():
            temp_str += i
        elif i == "," :
            temp.append(int(temp_str))
            temp_str = ""
        elif i == "}":
            if len(temp) != 0:
                temp.append(int(temp_str))
                temp_list.append(temp)
                temp = []
            elif temp_str != "":
                temp_list.append([int(temp_str)])
                temp = []
    sorted_temp_list = sorted(temp_list, key=lambda x:-len(x))
    for idx in range(len(sorted_temp_list)-1):
        element = set(sorted_temp_list[idx]).difference(set(sorted_temp_list[idx+1]))
        answer.append(element.pop())
    answer.append(sorted_temp_list[-1].pop())
    return answer[::-1]

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")) # [2, 1, 3, 4]
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")) # [2, 1, 3, 4]
print(solution("{{20,111},{111}}")) # 	[111, 20]
print(solution("{{123}}")) # [123]
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")) # [3, 2, 4, 1]