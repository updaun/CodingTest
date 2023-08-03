# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 조건 문자열
# https://school.programmers.co.kr/learn/courses/30/lessons/181934

def solution(ineq, eq, n, m):
    answer_dict = {
        ">=":int(n>=m),
        "<=":int(n<=m),
        ">!":int(n>m),
        "<!":int(n<m),
    }
    return answer_dict[ineq+eq]
        
# 다른 사람의 풀이
def solution(ineq, eq, n, m):
    return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))


q = solution("<", "=", 20, 50)
assert q == 1, "불일치"
print(q)

q = solution(">", "!", 41, 78)
assert q == 0, "불일치"
print(q)
