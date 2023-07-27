# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 추억 점수
# https://school.programmers.co.kr/learn/courses/30/lessons/181862


def solution(name, yearning, photo):
    score_dict = dict()
    for k, v in zip(name, yearning):
        score_dict[k] = v
    return [sum([score_dict[j] for j in i if j in score_dict.keys()]) for i in photo]


# 다른 사람의 풀이 (index 활용 - 이게 더 느림)
def solution(이름, 점수, 사진):
    return [sum(점수[이름.index(j)] for j in i if j in 이름) for i in 사진]


q = solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]])
assert q == [19, 15, 6], "불일치"
print(q)

q = solution(["kali", "mari", "don"], [11, 1, 55], [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]])
assert q == [67, 0, 55], "불일치"
print(q)

q = solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may"],["kein", "deny", "may"], ["kon", "coni"]])
assert q == [5, 15, 0], "불일치"
print(q)