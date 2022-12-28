# result = [0] * 3
# target = [1, 2, 3, 4, 5]
# def combination(N, M, level, idx):
#     if level == M:
#         print(result)
#         return
    
#     for i in range(idx, N):
#         result[level] = target[i]
#         combination(N, M, level+1, i+1)

# combination(5, 3, 0, 0)

def combination(number, level, idx, result):
    global answer
    if level == 3:
        if sum(result) == 0:
            answer.append(result)
        return
    
    for i in range(idx, len(number)):
        result[level] = number[i]
        combination(number, level+1, i+1, result)
    
answer = []

def solution(number):
    result = [0]*3    
    combination(number, 0, 0, result)
    return len(answer)