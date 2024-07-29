# 프로그래머스
# 코딩테스트 연습 > Summer/Winter Coding(~2018) > 영어 끝말잇기


def solution(n, words):
    a = []
    for i in range(len(words)):
        if words[i] not in a:
            if len(a) > 0:
                if a[-1][-1] != words[i][0]:
                    x, y = divmod(i, n)
                    return [y+1, x+1]
            a.append(words[i])
        else:
            x, y = divmod(i, n)
            return [y+1, x+1]
    return [0,0]
        
print(solution(["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])) # [3, 3]
print(solution(["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"])) # [0, 0]
print(solution(["hello", "one", "even", "never", "now", "world", "draw"])) # [1, 3]