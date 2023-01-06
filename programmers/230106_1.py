# 프로그래머스
# 코딩테스트 연습 > 해시 > 폰켓몬


def solution(nums):
    if len(nums) // 2 < len(set(nums)):
        return len(nums) // 2
    return len(set(nums))

print(solution([3,1,2,3])) # 2
print(solution([3,3,3,2,2,4])) # 3
print(solution([3,3,3,2,2,2])) # 2