# 프로그래머스
# 코딩테스트 연습 > 2018 KAKAO BLIND RECRUITMENT > [1차] 비밀지도


def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        b_a = ("0"*n + bin(a)[2:])[-n:]
        b_b = ("0"*n + bin(b)[2:])[-n:]
        answer.append("".join([" " if int(b_a[i]) + int(b_b[i]) == 0 else "#" for i in range(n)]))        
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])) # ["#####","# # #", "### #", "# ##", "#####"]
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10])) # ["######", "### #", "## ##", " #### ", " #####", "### # "]
