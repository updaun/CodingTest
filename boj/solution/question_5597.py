import sys
student = [i for i in range(1, 31)] 
for i in range(28):
    student.remove(int(sys.stdin.readline()))
print('\n'.join(map(str, sorted(student))))