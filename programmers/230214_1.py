# 프로그래머스
# 코딩테스트 연습 > 2022 KAKAO BLIND RECRUITMENT > k진수에서 소수 개수 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/92335

def solution(n, k):
    answer = []
    k_number = ""
    while n:
        n, r = divmod(n, k)
        k_number += str(r)
    k_number = k_number[::-1]
    n_list = k_number.split("0")
    for i in n_list:
        if i == "1" or i == "":
            continue
        p = int(i)
        temp = 2
        if p in answer:
            answer.append(temp)
        else:
            for temp in range(2, int(p**0.5)+1):
                if p % temp == 0:
                    break
            else:
                answer.append(p)
    return len(answer)


print(solution(437674, 3))  # 3
print(solution(110011, 10))  # 2
