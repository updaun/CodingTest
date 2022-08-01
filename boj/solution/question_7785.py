import sys
input = sys.stdin.readline
company = dict()
for i in range(int(input())):
    name, log = map(str, input().split())
    if log == 'enter':
        company[name] = 1
    else:
        company.pop(name)
print("\n".join(map(str, sorted(company, reverse=True))))

# import sys
# input = sys.stdin.readline
# company = []
# for i in range(int(input())):
#     name, log = map(str, input().split())
#     if log == 'enter':
#         company.append(name)
#     else:
#         company.remove(name)
# print("\n".join(map(str, sorted(company, reverse=True))))