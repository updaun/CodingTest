# 프로그래머스
# 코딩테스트 연습 > 2020 카카오 인턴십 > 키패드 누르기
# https://school.programmers.co.kr/learn/courses/30/lessons/67256

def get_distance(p1, p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])


def solution(numbers, hand):
    d = {
        0: [0, 0],
        1: [-1, 3],
        2: [0, 3],
        3: [1, 3],
        4: [-1, 2],
        5: [0, 2],
        6: [1, 2],
        7: [-1, 1],
        8: [0, 1],
        9: [1, 1],
        "*": [-1, 0],
        "#": [1, 0],
    }
    answer = ''
    l = '*'
    r = '#'
    for i in numbers:
        if i != 0 and i % 3 == 0:
            answer += 'R'
            r = i
        elif i % 3 == 1:
            answer += 'L'
            l = i
        else:
            if get_distance(d[i], d[r]) < get_distance(d[i], d[l]):
                answer += 'R'
                r = i
            elif get_distance(d[i], d[r]) > get_distance(d[i], d[l]):
                answer += 'L'
                l = i
            else:
                if hand == 'right':
                    answer += 'R'
                    r = i
                else:
                    answer += 'L'
                    l = i
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))  # "LRLLLRLLRRL"
assert solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],
                "right") == "LRLLLRLLRRL", "불일치"

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))  # "LRLLRRLLLRR"
assert solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],
                "left") == "LRLLRRLLLRR", "불일치"

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))  # "LLRLLRLLRL"
assert solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
                "right") == "LLRLLRLLRL", "불일치"
