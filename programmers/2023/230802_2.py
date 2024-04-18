# 프로그래머스
# 코딩테스트 연습 > 연습문제 > JadenCase 문자열 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    return " ".join([i.capitalize() for i in s.split(" ")])

# s.split() 과 s.split(" ")는 다르다.

q = solution("3people unFollowed me")
assert q == "3people Unfollowed Me", "불일치"
print(q)

q = solution("for the last week")
assert q == "For The Last Week", "불일치"
print(q)

q = solution("A ")
assert q == "A ", "불일치"
print(q)

