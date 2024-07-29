# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 1로 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/181880


def solution(num_list):
    answer = 0
    for i in num_list:
        while i != 1:
            if i % 2 == 0:
                i /= 2
            else:
                i -= 1
                i /= 2
            answer += 1
    return answer

# 다른 사람의 풀이 (O(nlogn) -> O(n))
def solution(num_list):
    return sum(len(bin(i)) - 3 for i in num_list)

q = solution([12, 4, 15, 1, 14])
assert q == 11, "불일치"
print(q)
