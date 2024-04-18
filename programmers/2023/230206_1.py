# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 연속 부분 수열 합의 개수

def solution(elements):
    answer = set()
    len_elements = len(elements)
    elements = elements*2
    for i in range(len_elements):
        for j in range(len_elements):
            answer.add(sum(elements[j:j+i+1]))
    return len(answer)

print(solution([7,9,1,1,4])) # 18