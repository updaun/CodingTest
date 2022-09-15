import sys
input = sys.stdin.readline

def backtracking():
    global count
    global triger
    if len(arr) == len(target):
        if count == int(n)-1:
            print(f"{target} {n} = "+"".join(map(str, [temp[i] for i in arr])))
            triger = True
            count = sys.maxsize
            return
        else:
            count += 1
            return
        
    for i in range(len(target)):
        if i not in arr:
            arr.append(i)
            backtracking()
            arr.pop()

while True:
    try:
        target, n = input().split()
    except:
        break

    temp = [target[i] for i in range(len(target))]
    arr = []
    count = 0
    triger = False

    backtracking()
    
    if triger==False and count < int(n)-1:
        print(f"{target} {n} = No permutation")