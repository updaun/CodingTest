import sys
input = sys.stdin.readline

def check(string_list, n):
    for i in range(n):
        a = ""
        b = ""
        for j in range(n):
            if j != i:
                a = string_list[i]
                b = string_list[j]
                test_list = [a+b, b+a]
                for test in test_list:
                    if test == test[::-1]:
                        return test
    else:
        return 0

for _ in range(int(input())):
    n = int(input())
    string_list = [input().rstrip() for i in range(n)]
    print(check(string_list, n))

        