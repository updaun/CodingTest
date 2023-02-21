# 프로그래머스
# 코딩테스트 연습 > 2018 KAKAO BLIND RECRUITMENT > [3차] 파일명 정렬
# https://school.programmers.co.kr/learn/courses/30/lessons/17686

def solution(files):
    heads = dict()
    numbers = dict()
    for file in files:
        head = ""
        number = ""
        t = False
        for s in file:
            if s.isdigit():
                number += s
                t = True
            else:
                if t:
                    break
                head += s
        heads[file] = head.lower()
        numbers[file] = int(number)
    return sorted(files, key=lambda x:(heads[x], numbers[x]))

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
# ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
# ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
