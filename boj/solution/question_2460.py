import sys
passenger = 0
max_passenger = 0 
for i in range(10):
    output_num, input_num = list(map(int, sys.stdin.readline().split()))
    passenger += input_num
    passenger -= output_num
    if max_passenger < passenger:
        max_passenger = passenger
print(max_passenger)