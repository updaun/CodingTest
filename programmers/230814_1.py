# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 뒤에 있는 큰 수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/154539

def solution(numbers):
    answer = []
    for i, n in enumerate(numbers):
        if n >= max(numbers[i:]):
            answer.append(-1)
        else:
            temp = numbers[i:]
            for t in temp:
                if t > n:
                    answer.append(t)
                    break
    return answer

q = solution([2, 3, 3, 5])
assert q == [3, 5, 5, -1], "불일치"
print(q)

q = solution([9, 1, 5, 3, 6, 2])
assert q == [-1, 5, 6, 6, -1, -1], "불일치"
print(q)
