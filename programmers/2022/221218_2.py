# 프로그래머스
# 코딩테스트 연습 > 코딩테스트 입문 > 최빈값 구하기

def solution(array):
    cnt_array = []
    set_cnt_array = []
    for i in array:
        cnt_array.append(array.count(i))
    for i in set(array):
        set_cnt_array.append(array.count(i))
    for i in set_cnt_array:
        if set_cnt_array.count(max(set_cnt_array)) != 1:
            return -1
    else:
        return array[cnt_array.index(max(cnt_array))]

print(solution([1, 2, 3, 3, 3, 4])) # 3
print(solution([1, 1, 2, 2])) # -1
print(solution([1])) # 1