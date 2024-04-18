# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 배열의 원소 삭제하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181844


def solution(arr, delete_list):
    # 1차 시도 : 정렬이 틀어져 실패
    # return list(set(arr).difference(set(delete_list)))
    for i in delete_list:
        if i in arr:
            arr.remove(i)
    return arr

    # 다른 사람의 풀이
    return [i for i in arr if i not in delete_list]

q = solution([293, 1000, 395, 678, 94], [94, 777, 104, 1000, 1, 12])
assert q == [293, 395, 678], "불일치"
print(q)

q = solution([110, 66, 439, 785, 1], [377, 823, 119, 43])
assert q == [110, 66, 439, 785, 1], "불일치"
print(q)
