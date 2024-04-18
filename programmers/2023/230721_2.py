# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 빈 배열에 추가, 삭제하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181860


def solution(arr, flag):
    X = []
    for i, b in enumerate(flag):
        if b:
            X += [arr[i]] * arr[i]*2
        else:
            for i in range(arr[i]):
                X.pop()
    return X


q = solution([3, 2, 4, 1, 3], [True, False, True, False, False])
assert q == [3, 3, 3, 3, 4, 4, 4, 4], "불일치"
print(q)
